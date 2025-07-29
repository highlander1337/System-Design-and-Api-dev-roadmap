def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)//2)
        
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)

def verify(result):
    if result:
        print(f'Target found!')
    else:
        print("Target not found in list")
        
my_list = range(0, 100)
my_target = 100

result = recursive_binary_search(my_list, my_target)

verify(result)