def solution():
    # initialize count and file content
    file_contents = []
    total = 0
    with open("file.txt") as file:
        for line in file:
            file_contents.append(line)
    
    
    idx = 0
    curr = 1
    num_set = []
    operation = ""
    while idx < len(file_contents[0]):

        # build current number and check to see if it is all blank (if it is, it marks the ending of a set)
        curr_string = ""
        for line in file_contents[0:len(file_contents)-1]:
            curr_string += line[idx]
        curr_string = curr_string.replace(" ", "")
        curr_string = curr_string.replace("\n", "")

        # if the end of a set has been reached, do calculations depending on current operator and add to the total
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

        # if not, add the current number to current set
        else:
            # check if the operator is found
            if file_contents[-1][idx - 1] in "*+":
                operation = file_contents[-1][idx - 1]
            num_set.append(curr_string)
        idx += 1
    
    print(total)

solution()