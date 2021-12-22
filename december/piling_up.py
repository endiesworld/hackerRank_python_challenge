local_input = " 1000000000" * 100000
blocks = []
blocks_sizes = []
test_cases = int(input())
test_condition = ["No" for i in range(test_cases)]
for i in range(test_cases):
    size = int(input())
    blocks_sizes.append(size)
    block = input().split()
    block_1 = [int(x) for x in block]
    blocks.append(block_1)

for index, ele in enumerate(blocks_sizes):
    left = 0
    right = -1
    move = 1
    arr = blocks[index]
    while move < ele:
        if arr[right] > arr[left]:
            if arr[right] > arr[right - 1]:
                move += 1
                right -= 1
            else:
                break
        elif arr[right] < arr[left]:
            if arr[left] > arr[left + 1]:
                move += 1
                left += 1
            else:
                break
        else:
            if ((arr[right] >= arr[right - 1])) & (arr[left] >= arr[left + 1]):
                move += 2
                right -= 1
                left += 1
            else:
                break
    print(f"You total numbers of move is {move}")
    print(f"number of element is  {ele}")
    if move >= ele:
        test_condition[index] = "Yes"

for i in test_condition:
    print(i)
