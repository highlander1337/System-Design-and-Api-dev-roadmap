
# Binary Search Algorithm with Complexity Annotations

This Python implementation of the Binary Search algorithm includes detailed comments explaining its **time** and **space** complexity. While this code is written in Python, the complexity analysis applies similarly to compiled languages such as **C++**, **Java**, **Rust**, and others.

## Binary Search Implementation

```python
def binary_search(list, target):
    """ 
    Performs binary search on a sorted list.

    Time Complexity:
    - Best Case: O(1) — When the target is at the midpoint in the first iteration.
    - Average Case: O(log n)
    - Worst Case: O(log n)

    Space Complexity:
    - O(1) — Iterative implementation uses constant space (no recursive stack).

    Note:
    - In languages like C++ and Java, this space complexity remains O(1) unless recursion is used.
    - Binary search requires the input list/array to be sorted beforehand.
    """
    
    # O(1) — Constant time to initialize variables
    first = 0 
    last = len(list) - 1 
    
    # Loop runs until the search space is exhausted
    while first <= last:
        # O(1) — Compute midpoint (same in Python, Java, C++)
        midpoint = (first + last) // 2  # Floor division
        
        # O(1) — Comparison operation
        if list[midpoint] == target:
            return midpoint  # Target found
        
        # O(1) — Decide whether to search left or right half
        elif list[midpoint] < target:
            first = midpoint + 1  # Eliminate left half
        else:
            last = midpoint - 1   # Eliminate right half
    
    # O(1) — Target not found
    return None
```

## Result Verification Function

```python
def verify(index):
    """
    Utility function to print the result.

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    if index is not None:
        print(f'Target found at index {index}!')
    else:
        print("Target not found in list")
```

## Example Execution

```python
my_list = range(0, 100)  # O(n) to generate, but only once. Range object in Python is lazy.
my_target = 12

result = binary_search(my_list, my_target)

verify(result)
```

---

## Cross-Language Notes

| Language | Iterative Binary Search Time | Recursive Binary Search Time | Space Complexity (Iterative) | Space Complexity (Recursive) |
|----------|------------------------------|-------------------------------|-------------------------------|-------------------------------|
| Python   | O(log n)                     | O(log n)                      | O(1)                          | O(log n) (due to recursion stack) |
| C++      | O(log n)                     | O(log n)                      | O(1)                          | O(log n)                        |
| Java     | O(log n)                     | O(log n)                      | O(1)                          | O(log n)                        |
| Go       | O(log n)                     | O(log n)                      | O(1)                          | O(log n)                        |
| Rust     | O(log n)                     | O(log n)                      | O(1)                          | O(log n)                        |

---

## Final Notes

- **Binary Search** is efficient for *read-heavy* scenarios with *sorted data*.
- For dynamic datasets that are frequently modified, consider using *balanced search trees* or *hash tables*.
- Avoid recursive versions in constrained-memory environments (like embedded systems) due to extra stack usage.
