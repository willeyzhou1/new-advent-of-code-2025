def solution():
    sum = 0
    with open("file.txt") as file:
        for line in file:
            number = str(line)
            l, r = 0, 1
            max_num = 0
            while r < len(number):
                curr_num = number[l] + number[r]
                max_num = max(int(curr_num), max_num)
                if number[r] > number[l] and r != len(number) - 1:
                    l = r
                r += 1
            sum += max_num
    
    print(sum)

solution()