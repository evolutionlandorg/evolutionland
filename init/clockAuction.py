from web3 import Web3, HTTPProvider
import rlp
import time
import json
import requests
from conf import conf
import util


class Auction:
    FirstAuctionTime = '2022-02-15 16:00:00'  # first Auction time
    w3 = Web3(HTTPProvider(conf.current["ETH_RPC"], request_kwargs={'timeout': 120}))
    firstAuctionTimeStamp = int(time.mktime(time.strptime(FirstAuctionTime, '%Y-%m-%d %H:%M:%S')))
    duration = 3600 * 6
    timeInterval = 3600  # Auction time interval second
    nonce = w3.eth.getTransactionCount(Web3.toChecksumAddress(conf.current["USER_ADDRESS"]))

    def run(self):
        with open('objectOwnership.abi', 'r') as objectOwnership_definition:
            objectOwnership_abi = json.load(objectOwnership_definition)

        objectOwnership = self.w3.eth.contract(address=Web3.toChecksumAddress(conf.current["ObjectOwnership"]),
                                               abi=objectOwnership_abi)

        ignoreCoord = []

        startingPriceInToken = util.toWei(3, conf.current.get("token_decimals", 18))
        endingPriceInToken = int(startingPriceInToken / 5)  # 拍卖价格是随着时间下降的，如果没有人拍后的最终价格
        nonceAdd = 0
        has_auction = 0
        lands = requests.get(conf.current["LAND_API"]).json()
        print(lands)
        for index, land in enumerate(lands["data"]):
            isSpecial = land["resource"][-3]
            coord = "{lon},{lat}".format(lon=land["lon"], lat=land["lat"])
            # if isSpecial == 1 or isSpecial == 2 or coord in ignoreCoord:  # Reserved land
            #     continue
            owner = objectOwnership.functions.ownerOf(int(land["token_id"], 16)).call()

            if owner.lower() != conf.current["GENESIS_HOLDER"].lower():
                print("已经上架")
                has_auction += 1
                continue
            has_auction += 1
            startAt = self.firstAuctionTimeStamp + self.timeInterval * (has_auction - 10)

            tokenId = land["token_id"]
            # createAuction(uint256,uint256,uint256,uint256,uint256,address)
            self.do(tokenId, startingPriceInToken, endingPriceInToken, startAt, self.duration, nonceAdd)
            nonceAdd += 1
            # if has_auction > 10:

            time.sleep(1)

    def do(self, tokenId, startingPriceInToken, endingPriceInToken, startAt, duration, nonceAdd):
        method = self.w3.sha3(text="createAuction(uint256,uint256,uint256,uint256,uint256,address)").hex()[0:10]
        execute_transaction = method + \
                              util.u256ToInput(int(tokenId, 16)) + \
                              util.u256ToInput(startingPriceInToken) + \
                              util.u256ToInput(endingPriceInToken) + \
                              util.u256ToInput(duration) + \
                              util.u256ToInput(startAt) + \
                              util.pandding(conf.current["RingTokenAddress"])
        # print("execute_transaction: ", execute_transaction)
        # print("nonce: ", self.nonce)
        params = dict(
            nonce=self.nonce + nonceAdd,
            gasPrice=10000000000,
            gas=1000000,
            to=conf.current["GENESIS_HOLDER"],
            data=execute_transaction,
            chainId=conf.current["NETWORK_ID"]
        )
        print("sign_transaction: ", params)

        signed = self.w3.eth.account.sign_transaction(params, conf.current["CREATE_PRI_KEY"])
        txid = self.w3.eth.send_raw_transaction(signed.rawTransaction).hex()
        print("txid: ", txid)


if __name__ == '__main__':
    auction = Auction()
    auction.run()
