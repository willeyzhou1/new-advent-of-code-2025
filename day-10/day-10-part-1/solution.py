def solution():
    # parse input
    machines = []
    total = 0
    with open("file.txt") as file:
        for line in file:
            line = line.strip().split(" ")
            machines.append(line)

    # for each machine, parse the button wirings and indicator lights and backtrack to find all cases where the intended state is found
    for machine in machines:
        intended_state = list(machine[0][1:len(machine[0])-1])
        machine = machine[1:len(machine)-1]
        machine_state = list("." * len(intended_state))
        num_counts = []

        # backtracking to find all instances where intended state is found and the number of switches flipped; add number to a list
        def backtrack(curr_state, intended_state, count, index):
            if curr_state == intended_state:
                num_counts.append(count)
                return
            if index == len(machine):
                return
            
            switch = machine[index]
            switch = switch.replace("(", "")
            switch = switch.replace(")", "").split(",")
            switch = [int(s) for s in switch]
            new_state = curr_state.copy()
            for number in switch:
                if new_state[number] == "#":
                    new_state[number] = "."
                else:
                    new_state[number] = "#"
            
            backtrack(new_state, intended_state, count + 1, index + 1)
            backtrack(curr_state, intended_state, count, index + 1)
        
        backtrack(machine_state, intended_state, 0, 0)
        total += min(num_counts)
    print(total)



solution()