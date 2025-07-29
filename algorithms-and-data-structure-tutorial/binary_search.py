def binary_search(list, target):
    """ 
    If found returns the index position of the target, else returns None
    """
    
    # O(1)
    first = 0 
    # O(1)
    last = len(list) - 1 
    
    while first <= last:
        # O(1)
        midpoint = (first + last)//2 # floor division operator
        
        # O(1)
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            # O(log n)
            first = midpoint + 1
        else:
            # O(log n)
            last = midpoint - 1
    
    return None

def verify(index):
    if index is not None:
        print(f'Target found at index {index}!')
    else:
        print("Target not found in list")
        
my_list = range(0, 100)
my_target = 12

result = binary_search(my_list, my_target)

verify(result)