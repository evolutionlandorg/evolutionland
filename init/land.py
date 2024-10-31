import json
import time

import rlp
from web3 import Web3, HTTPProvider

from conf import conf
import util


class Land:
    w3 = Web3(HTTPProvider(conf.current["ETH_RPC"], request_kwargs={'timeout': 120}))

    def run(self):
        with open('./abi/land.abi', 'r') as land_definition:
            land_abi = json.load(land_definition)
        with open(conf.current["RESOURCE_FILE"], 'r') as resource_definition:
            resource_json = json.load(resource_definition)
        resource_json = sorted(resource_json, key=lambda x: x["location_id"])
        land_contract = self.w3.eth.contract(address=Web3.toChecksumAddress(conf.current["Land_ADDRESS"]), abi=land_abi)

        nonceAdd = 0
        nonce = self.w3.eth.getTransactionCount(Web3.toChecksumAddress(conf.current["USER_ADDRESS"]))
        method = self.w3.sha3(text="assignNewLand(int256,int256,address,uint256,uint256)").hex()[0:10]

        for index, resource in enumerate(resource_json):
            x = resource["coordinate"]["x"]
            y = resource["coordinate"]["y"]
            landTokenId = land_contract.functions.getTokenIdByLocation(x, y).call()
            if landTokenId != 0:
                print("checkout coord", x, y, "already init land index", resource["location_id"])
                continue
            isSpecial = resource["isSpecial"]
            landRange = conf.current["RANGE"]
            if x == landRange[0] or x == landRange[1] or y == landRange[2] or y == landRange[3]:
                isSpecial = 4

            rate = resource["gold"] + (resource["wood"] << 16) + (resource["water"] << 32) + \
                   (resource["fire"] << 48) + (resource["earth"] << 64)
            execute_transaction = method + util.u256ToInput(x) + util.u256ToInput(y) + util.pandding(
                conf.current["GENESIS_HOLDER"]) + util.u256ToInput(rate) + util.u256ToInput(isSpecial)
            signed = self.w3.eth.account.sign_transaction(
                dict(
                    nonce=nonce + nonceAdd,
                    gasPrice=10000000000,
                    gas=1000000,
                    to=conf.current["Land_ADDRESS"],
                    data=execute_transaction,
                    chainId=conf.current["NETWORK_ID"]
                ), conf.current["CREATE_PRI_KEY"])
            nonceAdd += 1
            txid = self.w3.eth.send_raw_transaction(signed.rawTransaction).hex()
            print(resource, txid, "{x} {y}".format(x=x, y=y))
            # time.sleep(1)
            return


if __name__ == '__main__':
    Land().run()
