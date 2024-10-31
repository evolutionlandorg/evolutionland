import math
import decimal
from web3 import Web3


def write_to_file(des, content):
    fo = open(des, "a")
    fo.write(content)
    fo.write('\n')
    fo.close()


def pandding(s):
    if s.startswith('0x'):
        s = s[2:]
    return s.rjust(64, '0')


def pandding32(s):
    if s.startswith('0x'):
        s = s[2:]
    return s.rjust(32, '0')


def panddingF(s):
    if s.startswith('0x'):
        s = s[2:]
    return s.rjust(64, 'f')


def u256ToInput(u):
    if u >= 0:
        hex_str = "{:x}".format(u)
        return pandding(hex_str)
    else:
        if abs(u) == 1:
            hex_str = "{:x}".format(16 - abs(u))
        else:
            hex_str = "{:x}".format(int(pow(16, math.ceil(math.log(abs(u), 16))) + u))
        return panddingF(hex_str)


def toWei(number, decimals=18):
    if decimals == 18:
        return Web3.toWei(number, "ether")
    if isinstance(number, (bytes, str, bytearray, int,)):
        d_number = decimal.Decimal(value=number)
    elif isinstance(number, float):
        d_number = decimal.Decimal(value=str(number))
    elif isinstance(number, decimal.Decimal):
        d_number = number
    else:
        raise TypeError("Unsupported type.  Must be one of integer, float, or string")
    return int(d_number * decimal.Decimal("1" + "".join(["0" for i in range(decimals)])))

def LogAnalysis(log: str):
    log = log.lstrip("0x")
    result = []
    for i  in range(int(len(log) / 64)):
        result.append(log[int(i * 64) : int((i + 1) * 64)])
    return result


if __name__ == '__main__':
    assert Web3.toWei(18, "ether") == toWei(18)
    assert Web3.toWei(18.5, "ether") == toWei(18.5)
    assert Web3.toWei(18.5000002, "ether") == toWei(18.5000002)

    assert Web3.toWei(18, "nano") == toWei(18, 9)
    assert Web3.toWei(18.5, "nano") == toWei(18.5, 9)
    assert Web3.toWei(18.5000002, "nano") == toWei(18.5000002, 9)