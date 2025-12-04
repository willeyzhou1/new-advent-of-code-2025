def solution():
    #assemble input
    input = []
    curr_row = []
    with open("file.txt") as file:
        for line in file:
            curr_row = []
            for char in line:
                if char != "\n":
                    curr_row.append(char)
            input.append(curr_row)
    
    total = 0
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]
    for i in range(len(input)):
        for j in range(len(input[i])):
            count = 0
            for dir in directions:
                if i + dir[0] < 0 or i + dir[0] >= len(input[i]) or j + dir[1] < 0 or j + dir[1] >= len(input[i]):
                    continue
                elif input[i+dir[0]][j+dir[1]] == "@":
                    count += 1
            if input[i][j] == "@" and count < 4:
                total += 1
    print(total)

solution()