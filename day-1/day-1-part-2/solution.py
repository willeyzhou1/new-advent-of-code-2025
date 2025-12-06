def solution():
    zeroes = 0
    curr = 50
    with open("file.txt") as file:
        for line in file:
            direction = line[0]
            number = int(line[1:])
    #         if direction == "L":
    #             zeroes += abs((curr - int(number)) // 100)
    #             curr = (curr - int(number)) % 100
    #         else:
    #             zeroes += abs((int(number) + curr) // 100)
    #             curr = (curr + int(number)) % 100

            # manually turn the knobs one by one (i got real frustrated trying to do modulo stuff)
            while number > 0:
                if direction == "L":
                    curr -= 1
                    number -= 1
                else:
                    curr += 1
                    number -= 1
                
                if curr == 100:
                    curr = 0
                if curr == -1:
                    curr = 99
                
                if curr == 0:
                    zeroes += 1
    print(zeroes)

solution()