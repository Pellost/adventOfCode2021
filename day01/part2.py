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

def winsum(input:[]):
    result = 0
    for value in input:
        result = result + value
    return result

def winnext(input:[],line: int):
    if (len(input) < 3):
        input.append(line)
    else:
        del input[0]
        input.append(line)
    return input

def compute(input: str):
    lines = input.split("\n")
    lines = [int(x) for x in lines]
    preSum = None
    results = 0
    list = []

    for line in lines:
        if len(list) == 3 and preSum != None:
            nextsum = winsum(list)
            if preSum < nextsum:
                results = results + 1
        preSum = winsum(list)
        winnext(list,line)
    return results
    raise ValueError


@pytest.mark.parametrize("expected", [5])
def test_results(expected):
    assert compute(INPUT) == expected


if __name__ == '__main__':
    i = open(file='input.txt').read()
    print(compute(i))