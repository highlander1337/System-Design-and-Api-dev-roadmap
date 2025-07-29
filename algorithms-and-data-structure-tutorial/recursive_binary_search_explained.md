
# Recursive Binary Search Algorithm with Complexity Annotations

This Python implementation of the **Recursive Binary Search** algorithm includes detailed comments on **time** and **space** complexity. The complexity holds similarly across compiled languages like **C++**, **Java**, **Go**, and **Rust**, with differences in how slices/subarrays are handled.

## Recursive Binary Search Implementation

```python
def recursive_binary_search(list, target):
    """ 
    Performs recursive binary search on a sorted list.

    Time Complexity:
    - Best Case: O(1) — Target is found at the midpoint on the first call.
    - Average Case: O(log n)
    - Worst Case: O(log n)

    Space Complexity (Python):
    - O(log n) due to recursive call stack.
    - O(n) if list slicing is not optimized (new list copies on each recursive call).

    Space Complexity (C++/Java/Go):
    - O(log n) for call stack only, no slicing unless manually done.
    """
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)//2)
        
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                # Slicing creates a new sublist in Python (O(k) space and time)
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)
```

## Result Verification Function

```python
def verify(result):
    """
    Utility function to print the result.

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    if result:
        print(f'Target found!')
    else:
        print("Target not found in list")
```

## Example Execution

```python
my_list = range(0, 100)  # Python range is lazy, slicing converts to list implicitly
my_target = 100

result = recursive_binary_search(my_list, my_target)

verify(result)
```

---

## Cross-Language Notes

| Language | Time Complexity | Space Complexity (Call Stack) | Sublist Handling |
|----------|------------------|-------------------------------|------------------|
| Python   | O(log n)         | O(log n)                      | O(n log n) total if slicing isn't avoided |
| C++      | O(log n)         | O(log n)                      | No slicing by default |
| Java     | O(log n)         | O(log n)                      | No slicing unless implemented manually |
| Go       | O(log n)         | O(log n)                      | No slicing unless copied explicitly |
| Rust     | O(log n)         | O(log n)                      | Slices are references (efficient)        |

---

## Final Notes

- Avoid Python list slicing in performance-critical recursive functions.
- For optimal performance in Python, pass indices instead of slicing (convert to index-based recursion).
- Use iterative binary search to avoid call stack limits or stack overflow in environments with shallow recursion depth.
