def solution():
    # same parsing as part 1
    input = open("file.txt")
    input = input.replace(",", " ")
    input = input.split(" ")
    sum = 0
    for nums in input:
        nums = nums.split("-")
        low = int(nums[0])
        high = int(nums[1])
        while low < high:
            string = str(low)
            '''
            for each number, iterate through the first half of the number
            grab a substring from beginning to current index and check if the substring * however many times it takes
            for the length to equal the original number length equals the string
            '''
            for i in range(1, len(string) // 2 + 1):
                if len(string) % i != 0:
                    continue
                else:
                    new_string = string[:i] * (len(string) // i)
                    if new_string == string:
                        sum += low
                        break
            low += 1
        
    print(sum)

solution()