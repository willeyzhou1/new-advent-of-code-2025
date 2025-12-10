def rectangle_area(x1, y1, x2, y2):
    x_value = abs(x2 - x1) + 1
    y_value = abs(y2 - y1) + 1
    return x_value * y_value

def solution():
    # parse input
    coords = []
    max_num = 0
    with open("file.txt") as file:
        for line in file:
            coords.append(line.strip().split(","))
    coords = [[int(s[0]), int(s[1])] for s in coords]
    print(coords)

    for i in range(len(coords)):
        for j in range(i, len(coords)):
            curr_num = rectangle_area(coords[i][0], coords[i][1], coords[j][0], coords[j][1])
            max_num = max(curr_num, max_num)
    
    print(max_num)

solution()