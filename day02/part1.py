

INPUT = '''\
forward 5
down 5
forward 8
up 3
down 8
forward 2'''


def compute(input: str):
    lines = input.split("\n")
    lines = [x for x in lines]

    position = [0,0]

    for line in lines:
        position = parse(line, position)
    results = position[0] * position[1]
    return results
    raise ValueError


def parse(input: str, position: []):
    cmd = input.split(" ")
    # cmd[0] = command, cmd[1] = val
    match cmd[0]:
        case 'forward':
            position[0] += int(cmd[1])
        case 'down':
            position[1] += int(cmd[1])
        case 'up':
            position[1] -= int(cmd[1])
    return position

# @pytest.mark.parametrize("expected", [150])
# def test_results(expected):
#     assert compute(INPUT) == expected


if __name__ == '__main__':
    i = open(file='input.txt').read()
    print(compute(i))