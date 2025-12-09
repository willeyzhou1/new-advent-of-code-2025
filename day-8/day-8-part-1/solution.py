import math
import heapq

def calculate_distance(x1, y1, z1, x2, y2, z2):
    x_dist = (x2 - x1) ** 2
    y_dist = (y2 - y1) ** 2
    z_dist = (z2 - z1) ** 2
    return math.sqrt(x_dist + y_dist + z_dist)

def solution():
    # parse input
    CONNECTIONS_MAX_LENGTH = 1000
    MAX_LARGEST_CIRCUITS = 3
    total = 1
    boxes = []
    with open("file.txt") as file:
        for line in file:
            boxes.append(line.strip())
    
    # push everything onto a max heap
    stack = []
    heapq.heapify(stack)
    seen = set()

    for i in range(len(boxes)):
        check_box = boxes[i].split(",")
        for j in range(len(boxes)):
            if i == j:
                continue
            else:
                curr_box = boxes[j].split(",")
                curr_val = calculate_distance(int(check_box[0]), int(check_box[1]), int(check_box[2]), int(curr_box[0]), int(curr_box[1]), int(curr_box[2]))
                curr_val = -curr_val
                
                #make sure connection isnt already in the heap
                curr_connection = tuple(sorted([boxes[i], boxes[j]]))
                if curr_connection not in seen:
                    heapq.heappush(stack, (curr_val, (boxes[i], boxes[j])))
                    seen.add(curr_connection)
                if len(stack) > CONNECTIONS_MAX_LENGTH:
                    heapq.heappop(stack)
    
    #pop all items from heap and assemble connections
    connections = []
    while stack:
        curr_item = set(heapq.heappop(stack)[1])
        temp = []
        for element in connections:
            if not element.isdisjoint(curr_item):
                curr_item = element.union(curr_item)
            else:
                temp.append(element)

        temp.append(curr_item)
        connections = temp
    
    print(connections)

    #grab 3 largest circuits
    highest_length = []
    heapq.heapify(highest_length)
    for item in connections:
        heapq.heappush(highest_length, len(item))
        if len(highest_length) > MAX_LARGEST_CIRCUITS:
            heapq.heappop(highest_length)
    
    print(highest_length)
    
    while highest_length:
        curr_length = heapq.heappop(highest_length)
        total *= curr_length

    print(total)
        


            

    


solution()