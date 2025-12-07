import functools

def alternatesolution():

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
    
    # perform recursion while caching answers
    @functools.cache
    def recurse(i, j, splits):
        if i == len(beams) - 1 or j == 0 or j == len(beams[0]) - 1:
            return 0
        while beams[i][j] != "^":
            if i == len(beams) - 1 or j == 0 or j == len(beams[0]) - 1:
                return 0
            i += 1
        
        return 1 + recurse(i, j+1, splits) + recurse(i, j-1, splits)
    
    splits = recurse(1, len(beams) // 2 - 1, splits)
    print(splits + 1)

alternatesolution()