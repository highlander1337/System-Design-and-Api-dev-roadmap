def search_min_value(array):
    min_value = array[0]
    min_indice = 0

    for i in range(1, len(array)): # skip the 0 indice
        if array[i] < min_value:
            min_value = array[i]
            min_indice = i
    return min_indice

def selection_sort(array):
    new_array = []
    for i in range(len(array)):
        min_value = search_min_value(array)
        new_array.append(array.pop(min_value))
    
    return new_array

print(selection_sort([5, 3, 6, 2, 10]))
        
