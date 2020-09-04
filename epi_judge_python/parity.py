from test_framework import generic_test


def parity(x: int) -> int:
    # TODO - you fill in here.
    # XOR version
    # Word 의 parity는 모든 bit들을 가지고 xor 한 결과와 같다.
    # XOR는 commutative, associative 하므로, 아래와 같은 방식으로 계산할 수 있다.
    x ^= x >> 32 # 32bit 씩 나눠서 xor 함 하위 32bit만 유효 (상위 32bit는 그대로임. 0 들과 xor 했으므로)
    x ^= x >> 16 # 16bit 씩 나눠서 xor 하위 16bit 만 유효 (상위 48bit는 그대로)
    x ^= x >> 8 # 8bit
    x ^= x >> 4 # 4bit
    x ^= x >> 2 # 2bit
    x ^= x >> 1 # 1bit
    return x & 0x1


if __name__ == '__main__':
    # parity(0b01101110)
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
