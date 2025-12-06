from collections import defaultdict

def solution():
    file_contents = []
    total = 0
    with open("file.txt") as file:
        for line in file:
            file_contents.append(line)
    
    
    #better stupid solution incoming
    idx = 0
    curr = 1
    num_set = []
    operation = ""
    while idx < len(file_contents[0]):
        curr_string = ""
        for line in file_contents[0:len(file_contents)-1]:
            curr_string += line[idx]
        curr_string = curr_string.replace(" ", "")
        curr_string = curr_string.replace("\n", "")
        if curr_string == "":
            if operation == "*":
                for num in num_set:
                    if num == "":
                        curr = curr * 1
                    else:
                        curr = curr * int(num)
                total += curr
            else:
                for num in num_set:
                    if num != "":
                        curr += int(num)
                total += curr - 1
            num_set.clear()
            curr = 1
        else:
            if file_contents[-1][idx - 1] in "*+":
                operation = file_contents[-1][idx - 1]
            curr_num = ""
            for line in file_contents[0:len(file_contents)-1]:
                curr_num += line[idx]
            num_set.append(curr_num)
        idx += 1
    
    print(total)

solution()