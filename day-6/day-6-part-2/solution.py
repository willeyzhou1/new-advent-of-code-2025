from collections import defaultdict

def solution():
    numbers = defaultdict(list)
    file_contents = []
    total = 0
    with open("file.txt") as file:
        for line in file:
            file_contents.append(line)
    
    #stupid solution incoming
    idx = 0
    curr = 1
    num_set = []
    operation = ""
    while idx < len(file_contents[0]):
        if (file_contents[0][idx] == " " or file_contents[0][idx] == '\n') and (file_contents[1][idx] == " " or file_contents[1][idx] == '\n') and (file_contents[2][idx] == " " or file_contents[2][idx] == '\n') and (file_contents[3][idx] == " " or file_contents[3][idx] == '\n'):
            if operation == "*":
                for num in num_set:
                    if num == "":
                        curr = curr * 1
                    else:
                        print(int(num))
                        curr = curr * int(num)
                total += curr
            else:
                for num in num_set:
                    if num != "":
                        curr += int(num)
                total += curr - 1
            print(curr)
            num_set.clear()
            curr = 1
        else:
            if file_contents[4][idx - 1] == "*" or file_contents[4][idx - 1] == "+":
                operation = file_contents[4][idx - 1]
                print(operation)
            
            num_set.append(file_contents[0][idx] + file_contents[1][idx] + file_contents[2][idx] + file_contents[3][idx])
            print(num_set)
        
        idx += 1



    #assemble numbers

    # for key, value in numbers.items():
    #     new_nums = []
    #     variable = ""
    #     max_len = 0
    #     to_replace = defaultdict(list)
    #     for num in value:
    #         max_len = max(max_len, len(num))
    #     for num in value:
    #         if num == "*" or num == "+":
    #             variable = num
    #             break
    #         num = num[::-1]
    #         for i in range(max_len - len(num), len(num)):
    #             to_replace[i].append(num[i])
            
    #         # print(to_replace)
    #     for value in to_replace.values():
    #         new_nums.append("".join(value))
    #     new_nums.append(variable)
    #     print(new_nums)
    #     numbers[key] = new_nums

    # print(numbers)
    # for value in numbers.values():
    #     if value[-1] == "*":
    #         for i in range(len(value) - 1):
    #             curr = curr * int(value[i])
    #     elif value[-1] == "+":
    #         for i in range(len(value) - 1):
    #             curr += int(value[i])
    #         curr -= 1
    #     total += curr
    #     curr = 1
    print(total)

solution()