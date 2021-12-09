import pytest

INPUT = '''\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''


def compute(input: str):
    lines = input.split("\n")
    lines = [x for x in lines]
    bitcount = None
    threshold = None
    gamma = ''
    inverse = ''

    for line in lines:
        if bitcount == None:
            binlength = len(line)
            bitcount = [0] * binlength
            threshold = list(range(binlength))

        for k in threshold:
            n = int(line,2)
            value = (n & (1 << (k))) >> (k)
            if value == 1:
                bitcount[k] += 1

            if bitcount[k] >= len(lines)/2:
                threshold.remove(k)

    for gammabit in bitcount:
        if gammabit >= len(lines)/2:
            gamma = '1' + gamma
        else:
            gamma = '0' + gamma
        inverse = '1' + inverse

    gamma = '0b' + gamma
    inverse = '0b' + inverse

    epsilon = int(gamma,2) ^ int(inverse,2)
    results = int(gamma,2) * epsilon

    return results
    raise ValueError


@pytest.mark.parametrize("expected", [198])
def test_results(expected):
    assert compute(INPUT) == expected


if __name__ == '__main__':
    i = open(file='input.txt').read()
    print(compute(i))