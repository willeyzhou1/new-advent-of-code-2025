from collections import defaultdict

def solution():
    numbers = defaultdict(list)
    total = 0
    curr = 1
    # assemble dictionary containing all numbers and operator
    with open("file.txt") as file:
        for line in file:
            line = line.strip(" ").split()
            for i in range(len(line)):
                numbers[i].append(line[i])
                
    # add or multiply each set of numbers depending on operator
    for value in numbers.values():
        if value[-1] == "*":
            for i in range(len(value) - 1):
                curr = curr * int(value[i])
        elif value[-1] == "+":
            for i in range(len(value) - 1):
                curr += int(value[i])
            curr -= 1
        total += curr
        curr = 1
    print(total)

solution()