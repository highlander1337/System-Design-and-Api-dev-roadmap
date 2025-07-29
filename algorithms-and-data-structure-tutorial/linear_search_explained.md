
# Linear Search Algorithm with Complexity Annotations

This Python implementation of the Linear Search algorithm includes detailed comments explaining its **time** and **space** complexity. These analyses are consistent across languages like **Python**, **C++**, **Java**, and others.

## Linear Search Implementation

```python
def linear_search(list, target):
    """ 
    Performs a linear search to find the target in the list.

    Time Complexity:
    - Best Case: O(1) — Target is at the beginning of the list.
    - Average Case: O(n)
    - Worst Case: O(n) — Target is at the end or not present.

    Space Complexity:
    - O(1) — No additional memory is used beyond loop counters and references.

    Notes:
    - Works on unsorted lists.
    - No assumptions are made about the data structure except indexability (arrays, lists, etc.).
    """
    
    # O(n) loop through the entire list
    for i in range(0, len(list)):
        if list[i] == target:
            return i  # O(1) if match found
    
    return None  # O(1) if match not found
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
my_list = range(0, 100)  # O(n) to generate, lazy range object in Python
my_target = 100

result = linear_search(my_list, my_target)

verify(result)
```

---

## Cross-Language Notes

| Language | Time Complexity (Best) | Time Complexity (Worst) | Space Complexity |
|----------|------------------------|--------------------------|------------------|
| Python   | O(1)                   | O(n)                     | O(1)             |
| C++      | O(1)                   | O(n)                     | O(1)             |
| Java     | O(1)                   | O(n)                     | O(1)             |
| Go       | O(1)                   | O(n)                     | O(1)             |
| Rust     | O(1)                   | O(n)                     | O(1)             |

---

## Final Notes

- Linear search is optimal for **small**, **unsorted** datasets.
- For large or sorted datasets, prefer **binary search** or more advanced structures (hash maps, search trees).
- Universally supported and easy to implement in any programming language.
