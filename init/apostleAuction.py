from web3 import Web3, HTTPProvider
from conf import conf
import time
import util
import json


class Auction:
    """将生成好的使徒, 放在拍卖市场中
    """
    w3 = Web3(HTTPProvider(conf.current["ETH_RPC"], request_kwargs={'timeout': 120}))
    timeInterval = 1200

    start_price = util.toWei(2, conf.current.get("token_decimals", 18))
    end_price = util.toWei(1, conf.current.get("token_decimals", 18))
    duration = 3600 * 12

    def run(self):

        nonceAdd = 0
        nonce = self.w3.eth.getTransactionCount(Web3.toChecksumAddress(conf.current["USER_ADDRESS"]))

        method = self.w3.sha3(text="createGen0Auction(uint256,uint256,uint256,uint256,uint256,address)").hex()[0:10]
        num_auction = 0

        initCount = 40
        sendCount = 0
        sendMaxCount = 40
        num_token = 160
        interval = 3600 * 11  # 11 hours
        day = 3600 * 24
        with open('objectOwnership.abi', 'r') as objectOwnership_definition:
            objectOwnership_abi = json.load(objectOwnership_definition)
        objectOwnership = self.w3.eth.contract(address=Web3.toChecksumAddress(conf.current["ObjectOwnership"]), abi=objectOwnership_abi)
        startAt = int(time.mktime(time.strptime('2021-09-01 21:00:00', '%Y-%m-%d %H:%M:%S')))

        Step = [False, False, False, False, True, True, True, True]
        while num_auction != initCount and sendCount < sendMaxCount:
            num_token += 1
            tokenId = conf.current["PREFIX"]
            num_token_value = hex(num_token)[2:].rjust(32, '0')
            tokenId += num_token_value
            try:
                owner = objectOwnership.functions.ownerOf(int(tokenId, 16)).call()
            except BaseException as e:
                print('%d ownerOf try failed in %s: %s' % (num_token, tokenId, e))
                break
            if owner == conf.current["Gen0_ADDRESS"]:
                start_at = startAt + day * int(num_auction / 8)
                if Step[num_auction % 8] is True:
                    start_at = start_at + interval

                print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_at)))

                execute_transaction = method + \
                                      util.u256ToInput(int(tokenId, 16)) + \
                                      util.u256ToInput(self.start_price) + \
                                      util.u256ToInput(self.end_price) + \
                                      util.u256ToInput(self.duration) + \
                                      util.u256ToInput(int(start_at)) + \
                                      util.pandding(conf.current["RingTokenAddress"])

                params = dict(
                    nonce=nonce + nonceAdd,
                    gasPrice=10000000000,
                    gas=1000000,
                    to=conf.current["Gen0_ADDRESS"],
                    data=execute_transaction,
                    chainId=conf.current["NETWORK_ID"]
                )
                print(params)
                signed = self.w3.eth.account.sign_transaction(params, conf.current["CREATE_PRI_KEY"])

                nonceAdd += 1
                num_auction += 1
                sendCount += 1
                print("send one", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_at)), tokenId, sendCount)

                print("txid:", self.w3.eth.send_raw_transaction(signed.rawTransaction).hex())
                return
                # time.sleep(3)
            else:
                print('%d try failed because owner is %s' % (num_token, owner))


if __name__ == '__main__':
    Auction().run()
