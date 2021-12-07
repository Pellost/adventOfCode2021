

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

    # distance, depth, aim
    position = [0,0,0]

    for line in lines:
        position = parse(line, position)
    results = position[0] * position[1]
    return results
    raise ValueError


def parse(input: str, position: []):
    cmd = input.split(" ")
    # cmd[0] = command, cmd[1] = val
    val = int(cmd[1])
    match cmd[0]:
        case 'forward':
            position[0] += val
            position[1] += position[2] * val
        case 'down':
            position[2] += val
        case 'up':
            position[2] -= val
    return position

# @pytest.mark.parametrize("expected", [150])
# def test_results(expected):
#     assert compute(INPUT) == expected

if __name__ == '__main__':
    i = open(file='input.txt').read()
    print(compute(i))