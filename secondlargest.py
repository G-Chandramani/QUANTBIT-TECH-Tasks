#Task3 Find the Second Largest Numbers in a list
def second_largest(list1):
    largest = second_largest = None
    
    for num in list1: 
        if largest is None or num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None or num > second_largest:
           
            if num != largest: 
                second_largest = num  
    return second_largest

list1 = [10, 20, 4, 45, 99]
print(second_largest(list1))
