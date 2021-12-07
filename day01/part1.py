import pytest

INPUT = '''\
199
200
208
210
200
207
240
269
260
263'''



def compute(input: str):
    lines = input.split("\n")
    lines = [int(x) for x in lines]
    preLine = None
    results = 0
    for line in lines:
        if preLine != None and line > preLine:
            results = results + 1
        preLine = line
    return results
    raise ValueError


@pytest.mark.parametrize("expected", [7])
def test_results(expected):
    assert compute(INPUT) == expected


if __name__ == '__main__':
    i = open(file='input.txt').read()
    print(compute(i))