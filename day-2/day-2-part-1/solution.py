def solution():
    input = open("file.txt")
    input = input.replace(",", " ")
    input = input.split(" ")
    sum = 0
    for range in input:
        range = range.split("-")
        low = int(range[0])
        high = int(range[1])
        while low < high:
            curr_num = str(low)
            mid = len(curr_num) // 2
            num1 = curr_num[0:mid]
            num2 = curr_num[mid:]
            if num1 == num2:
                sum += low
            low += 1
    print(sum)

solution()