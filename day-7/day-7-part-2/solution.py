def solution():
    # parse input
    beams = []
    splits = 0
    with open("file.txt") as file:
        for line in file:
            curr_row = []
            for char in line:
                if char != "\n":
                    if char == ".":
                        curr_row.append(0)
                    else:
                        curr_row.append(char)
            beams.append(curr_row)

    # Set base case: index right below the S is a path
    beams[1][len(beams) // 2 - 1] = 1

    # dynamically add number of paths to get to a certain index
    for i in range(2, len(beams)):
        for j in range(0, len(beams[0]) - 1):
            if beams[i][j] != "^":
                # general method: for every index, add the number above index + number above any "^" adjacent to it
                if beams[i][j+1] == "^" and beams[i][j-1] == "^":
                    beams[i][j] = beams[i-1][j+1] + beams[i-1][j-1] + beams[i-1][j]
                elif beams[i][j+1] == "^":
                    beams[i][j] = beams[i-1][j+1] + beams[i-1][j]
                elif beams[i][j-1] == "^":
                    beams[i][j] = beams[i-1][j-1] + beams[i-1][j]
                else:
                    if beams[i-1][j] != "^":
                        beams[i][j] = beams[i-1][j]
    
    # add up all paths to each index at the very last row
    for item in beams[-1]:
        splits += item

    print(beams)
    print(splits + 1)

solution()