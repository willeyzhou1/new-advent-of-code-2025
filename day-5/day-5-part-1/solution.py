def solution():
    checker = []
    total = 0

    # parse ranges
    with open("file1.txt") as file:
        for line in file:
            checker.append(line)

    # For each number, loop through list of ranges and check if it falls in between one of them
    with open("file2.txt") as file2:
        for line in file2:
            curr_num = int(line)
            print("current number checking: " + line)
            for range in checker:
                range = range.split("-")
                print(str(range[0]) + " " + str(range[1]))
                if int(range[0]) <= curr_num and int(range[1]) >= curr_num:
                    total += 1
                    break
    
    print(total)

solution()