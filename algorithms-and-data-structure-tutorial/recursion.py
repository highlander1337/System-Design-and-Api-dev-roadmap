def my_sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr.pop(0) + my_sum(arr)
        
print(my_sum([2, 3, 4]))


def my_count(arr):
    if arr == []:
        return 0
    else:
        arr.pop()
        return 1 + my_count(arr)
        
print(my_count([2, 3, 4, 5, 9]))

def my_max(arr):
    if len(arr) == 1:  # base case
        return arr[0]
    else:
        sub_max = my_max(arr[1:])  # recursive call
        if arr[0] > sub_max:
            return arr[0]
        else:
            return sub_max


print(my_max([5, 4, 3, 2, 9, 10]))  # Output: 10
