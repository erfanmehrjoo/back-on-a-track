# a function that takes a list and target parameter
# multiple viriable : middle , start , end , steps
# recursion or while loop
# increase steps each time a spilt is done 
# conditions to track target position
def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list) - 1
    steps = 0
    
    while(start <= end):
        print("Step",steps,":",list[start:end+1])
        
        steps += 1
        middle = (start + end) // 2
        
        if(list[middle] == element):
            return middle
        elif(list[middle] > element):
            end = middle - 1
        else:
            start = middle + 1
    return -1
# test part that you can change it as you like 
list = [1,2,3,4,5,6,7,8,9,10]
print(binary_search(list, 3))