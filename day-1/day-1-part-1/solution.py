def solution():
    zeroes = 0
    curr = 50
    with open("file.txt") as file:
        for line in file:
            direction = line[0]
            number = line[1:]
            # update current number based on direction
            if direction == "L":
                curr = (curr - int(number)) % 100
            else:
                curr = (curr + int(number)) % 100
            if curr == 0:
                zeroes += 1
    print(zeroes)

solution()