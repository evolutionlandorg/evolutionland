import time
from web3 import Web3, HTTPProvider
import util
from conf import conf


class Apostle:
    w3 = Web3(HTTPProvider(conf.current["ETH_RPC"]))

    genes = [
        # example: ["19499536473417985868022279319628700159664502873051349611308421073504278564", "1547501714072096020070343693"],
        
    ]



    def run(self):
        nonceAdd = 10
        print(conf.current["USER_ADDRESS"], conf.current["ETH_RPC"])
        nonce = self.w3.eth.getTransactionCount(Web3.toChecksumAddress(conf.current["USER_ADDRESS"]))
        method = self.w3.sha3(text="createGen0Apostle(uint256,uint256,address)").hex()[0:10]
        for i, v in enumerate(self.genes):
            if i == 20:
                break
            execute_transaction = method + \
                                  util.u256ToInput(int(v[0])) + \
                                  util.u256ToInput(int(v[1])) + \
                                  util.pandding(conf.current["GENESIS_HOLDER"])

            signed = self.w3.eth.account.sign_transaction(dict(
                nonce=nonce + nonceAdd,
                # maxFeePerGas=20000000000,
                # maxPriorityFeePerGas=20000000000,
                # gasPrice=30000000000, # crab
                gasPrice=10000000000,  # heco
                # gasPrice=self.w3.eth.gasPrice,  # mumbai
                gas=1000000,
                to=Web3.toChecksumAddress(conf.current["Gen0_ADDRESS"]),
                data=execute_transaction,
                chainId=conf.current["NETWORK_ID"],
            ), conf.current["CREATE_PRI_KEY"])
            print(self.w3.eth.send_raw_transaction(signed.rawTransaction).hex(), int(v[0]), i)
            nonceAdd += 1
            time.sleep(1)
            # return


if __name__ == '__main__':
    Apostle().run()
