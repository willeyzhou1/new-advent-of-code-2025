def solution():
    sum = 0
    with open("file.txt") as file:
        for line in file:
            max_num = 0
            number = list(str(line))
            if len(number) == 101:
                number = number[:-1]
            stack = []
            max_pop = len(number) - 13
            for digit in number:
                while max_pop >= 0 and stack and digit != "\n" and int(stack[-1]) < int(digit):
                    stack.pop()
                    max_pop -= 1
                if digit != "\n":
                    stack.append(digit)
            stack = stack[:12]
            max_num = int("".join(stack))
            sum += max_num
    print(sum)

solution()