# Selection Sort Algorithm with Complexity Annotations

This Python implementation of the **Selection Sort** algorithm includes detailed comments on **time** and **space** complexity. The analysis applies similarly to compiled languages like **C++**, **Java**, **Go**, and **Rust**, with differences mostly in memory allocation for dynamic arrays.

## Helper Function: Search Minimum Value

```python
def search_min_value(array):
    """
    Finds the index of the minimum value in the array.

    Time Complexity:
    - Best/Average/Worst Case: O(n) — must inspect every element.
    
    Space Complexity:
    - O(1) — only stores min_value and min_index.
    """
    min_value = array[0]
    min_indice = 0

    for i in range(1, len(array)):
        if array[i] < min_value:
            min_value = array[i]
            min_indice = i
    return min_indice
```

---

## Selection Sort Implementation

```python
def selection_sort(array):
    """
    Sorts an array by repeatedly selecting the minimum element
    and building a new sorted array.

    Time Complexity:
    - Best Case: O(n^2) — Even if array is sorted, each pass finds min value.
    - Average Case: O(n^2)
    - Worst Case: O(n^2)

    Space Complexity (Python):
    - O(n) — a new array is created for sorted elements.
    - O(1) if done in-place (classic selection sort variant).

    Note:
    - Using array.pop(min_index) modifies the original array.
    """
    new_array = []
    for i in range(len(array)):
        min_value = search_min_value(array)
        new_array.append(array.pop(min_value))
    
    return new_array
```

---

## Example Execution

```python
unsorted_array = [5, 3, 6, 2, 10]

sorted_array = selection_sort(unsorted_array)
print(sorted_array)
# Output: [2, 3, 5, 6, 10]
```

---

## Cross-Language Notes

| Language | Time Complexity | Space Complexity | Notes                                                                |
| -------- | --------------- | ---------------- | -------------------------------------------------------------------- |
| Python   | O(n^2)          | O(n) (new array) | array.pop() shifts elements each removal (O(n)), increasing overhead |
| C++      | O(n^2)          | O(1) (in-place)  | Typically done in-place using swaps                                  |
| Java     | O(n^2)          | O(1) (in-place)  | Same as C++                                                          |
| Go       | O(n^2)          | O(1) (in-place)  | Can implement in-place with slice swaps                              |
| Rust     | O(n^2)          | O(1) (in-place)  | Efficient in-place swaps with mutable slices                         |

---

## Final Notes

* Selection Sort is **simple** but **inefficient for large arrays** due to O(n²) time complexity.
* Avoid creating new arrays or using pop in Python for performance-critical code; instead, implement **in-place swaps**.
* Unlike binary search, selection sort **does not require the array to be sorted beforehand**.
* Suitable for small datasets or educational purposes, but not recommended for performance-critical applications.
