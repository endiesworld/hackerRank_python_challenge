num_cubes = []
blocks = []
test_output = []
num_test = int(input())
for i in range(num_test):
    n_cubes = int(input())
    num_cubes.append(n_cubes)
    block_input = input()
    block = [int(x) for x in block_input]
    blocks.append(block)


def left_side(x, y):
    return x > y


def right_side(x, y):
    return x > y


left_count = 0
right_count = 1
block = blocks[0]

