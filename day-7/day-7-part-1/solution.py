def solution():
    # parse input
    beams = []
    splits = 0
    with open("file.txt") as file:
        for line in file:
            curr_row = []
            for char in line:
                if char != "\n":
                    curr_row.append(char)
            beams.append(curr_row)
    beams[1][len(beams) // 2 - 1] = "|"

    # assemble beams while counting each instance where a beam encounters "^"
    for i in range(2, len(beams)):
        for j in range(0, len(beams[0])):
            if beams[i-1][j] == "|":
                if beams[i][j] == "^":
                    splits += 1
                    beams[i][j+1] = "|"
                    beams[i][j-1] = "|"
                if beams[i][j] == ".":
                    beams[i][j] = "|"
    
    print(beams)
    
    print(splits)


solution()