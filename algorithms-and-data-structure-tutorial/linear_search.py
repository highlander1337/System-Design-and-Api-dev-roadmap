def linear_search(list, target):
    """ 
    If found returns the index position of the target, else returns None
    """
    
    
    for i in range(0, len(list)):
        if list[i] == target:
            return i
        
    
    return None

def verify(index):
    if index is not None:
        print(f'Target found at index {index}!')
    else:
        print("Target not found in list")
        
my_list = range(0, 100)
my_target = 100

result = linear_search(my_list, my_target)

verify(result)