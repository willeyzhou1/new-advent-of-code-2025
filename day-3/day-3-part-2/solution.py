def solution():
    sum = 0
    with open("file.txt") as file:
        for line in file:
            # parse current line
            max_num = 0
            number = list(str(line))
            if len(number) == 101:
                number = number[:-1]
            
            # Add numbers to the stack and remove any numbers from the top that are less than the current digit if there are pops remaining
            stack = []
            max_pop = len(number) - 13
            for digit in number:
                while max_pop >= 0 and stack and digit != "\n" and int(stack[-1]) < int(digit):
                    stack.pop()
                    max_pop -= 1
                if digit != "\n":
                    stack.append(digit)
            
            # Ensure you get the biggest 12 digits
            stack = stack[:12]
            max_num = int("".join(stack))
            sum += max_num
    print(sum)

solution()