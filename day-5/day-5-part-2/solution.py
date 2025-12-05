def solution():
    ranges = []
    answer = []
    total = 0
    with open("file.txt") as file:
        for line in file:
            line = line.split("-")
            lower = int(line[0])
            higher = int(line[1])
            ranges.append([lower, higher])
    ranges.sort()
    curr_range = ranges[0]
    for range in ranges[1:]:
        if curr_range[1] >= range[0]:
            curr_range[1] = max(curr_range[1], range[1])
        else:
            answer.append(curr_range)
            curr_range = range
    
    answer.append(curr_range)
    print(answer)
    for num in answer:
        total += num[1] - num[0] + 1
    print(total)
solution()