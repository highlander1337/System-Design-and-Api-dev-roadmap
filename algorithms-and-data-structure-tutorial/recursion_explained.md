# Recursive List Processing Algorithms with Complexity Annotations

This file presents three recursive algorithms — **sum of elements**, **counting elements**, and **finding maximum value** in a list — with detailed annotations of **time** and **space** complexity.
The complexity holds similarly across compiled languages like **C++**, **Java**, **Go**, and **Rust**, with minor implementation differences in memory handling.

---

## 1. Recursive Sum of Elements

```python
def my_sum(arr):
    """
    Recursively computes the sum of elements in a list.

    Base Case:
    - If the list is empty, return 0.

    Recursive Case:
    - Remove the first element, add it to the recursive sum of the rest.

    Time Complexity:
    - Best/Average/Worst Case: O(n)
      Each recursive call processes one element.
    
    Space Complexity (Python):
    - O(n) due to recursion stack (one frame per element).
    - Additional overhead since arr.pop(0) is O(n) (shifts elements).
    """
    if len(arr) == 0:
        return 0
    else:
        return arr.pop(0) + my_sum(arr)
        
print(my_sum([2, 3, 4]))  # Output: 9
```

---

## 2. Recursive Count of Elements

```python
def my_count(arr):
    """
    Recursively counts the number of elements in a list.

    Base Case:
    - If the list is empty, return 0.

    Recursive Case:
    - Remove one element, add 1, and recurse on the remaining list.

    Time Complexity:
    - Best/Average/Worst Case: O(n)
      Each recursive call processes one element.
    
    Space Complexity (Python):
    - O(n) due to recursion stack.
    - arr.pop() from the end is O(1), so no shifting overhead.
    """
    if arr == []:
        return 0
    else:
        arr.pop()
        return 1 + my_count(arr)
        
print(my_count([2, 3, 4, 5, 9]))  # Output: 5
```

---

## 3. Recursive Maximum Value

```python
def my_max(arr):
    """
    Recursively finds the maximum value in a list.

    Base Case:
    - If the list has only one element, return it.

    Recursive Case:
    - Find the maximum of the rest of the list,
      then compare it with the current element.

    Time Complexity:
    - Best/Average/Worst Case: O(n)
      Each element must be compared once.
    
    Space Complexity (Python):
    - O(n) due to recursion stack.
    - Slicing arr[1:] creates a new list each call (O(n) overhead per call),
      leading to O(n^2) total space in Python.
    """
    if len(arr) == 1:
        return arr[0]
    else:
        sub_max = my_max(arr[1:])
        if arr[0] > sub_max:
            return arr[0]
        else:
            return sub_max

print(my_max([5, 4, 3, 2, 9, 10]))  # Output: 10
```

---

## Cross-Language Notes

| Language | my\_sum                                             | my\_count             | my\_max                                 | Notes                                                           |
| -------- | --------------------------------------------------- | --------------------- | --------------------------------------- | --------------------------------------------------------------- |
| Python   | O(n) time, O(n) space (extra O(n²) if slicing used) | O(n) time, O(n) space | O(n) time, O(n²) space (due to slicing) | `list.pop(0)` is costly (O(n)); prefer indexing for efficiency  |
| C++      | O(n) time, O(n) stack space                         | O(n) time, O(n) space | O(n) time, O(n) space                   | Works efficiently with pointers/iterators (no slicing overhead) |
| Java     | O(n) time, O(n) stack space                         | O(n) time, O(n) space | O(n) time, O(n) space                   | Similar to C++; arrays have fixed size                          |
| Go       | O(n) time, O(n) stack space                         | O(n) time, O(n) space | O(n) time, O(n) space                   | Slices avoid costly element shifts when indexed                 |
| Rust     | O(n) time, O(n) stack space                         | O(n) time, O(n) space | O(n) time, O(n) space                   | Borrowing slices avoids unnecessary allocations                 |

---

## Final Notes

* Recursive algorithms are **intuitive** but can be **inefficient in Python** due to:

  * Costly list slicing (`arr[1:]`).
  * Costly `pop(0)` shifting all elements.
* For **performance-critical code**, prefer:

  * Passing an **index parameter** instead of slicing.
  * Iterative solutions to avoid recursion depth limits.
* These recursive functions are excellent for **learning recursion** and **understanding base vs recursive cases**, even if not optimal for production.

---

# Optimized Recursive List Processing with Index Parameter

This section presents **optimized recursive algorithms** for computing the **sum of elements**, **counting elements**, and **finding the maximum value** in a list.
Instead of modifying the list (`pop`, slicing), these versions use an **index parameter** to track progress.
This improves efficiency, avoids creating new lists, and keeps the complexity at **O(n) time and O(n) space** across languages.

---

## 1. Recursive Sum of Elements (Index-Based)

```python
def my_sum(arr, i=0):
    """
    Recursively computes the sum of elements in a list
    using an index instead of modifying the list.

    Base Case:
    - If index reaches the end of the list, return 0.

    Recursive Case:
    - Return current element + recursive sum of the rest.

    Time Complexity:
    - O(n) — each element is visited once.
    
    Space Complexity:
    - O(n) — recursion stack (one frame per element).
    """
    if i == len(arr):  # reached end
        return 0
    return arr[i] + my_sum(arr, i+1)


print(my_sum([2, 3, 4]))  # Output: 9
```

---

## 2. Recursive Count of Elements (Index-Based)

```python
def my_count(arr, i=0):
    """
    Recursively counts the number of elements in a list
    using an index instead of popping elements.

    Base Case:
    - If index reaches the end, return 0.

    Recursive Case:
    - Add 1 and recurse to the next index.

    Time Complexity:
    - O(n) — must visit each element.
    
    Space Complexity:
    - O(n) — recursion stack.
    """
    if i == len(arr):
        return 0
    return 1 + my_count(arr, i+1)


print(my_count([2, 3, 4, 5, 9]))  # Output: 5
```

---

## 3. Recursive Maximum Value (Index-Based)

```python
def my_max(arr, i=0):
    """
    Recursively finds the maximum value in a list
    using an index instead of slicing.

    Base Case:
    - If index is the last element, return it.

    Recursive Case:
    - Compare current element with recursive maximum of the rest.

    Time Complexity:
    - O(n) — each element must be compared.
    
    Space Complexity:
    - O(n) — recursion stack.
    """
    if i == len(arr) - 1:  # last element
        return arr[i]

    sub_max = my_max(arr, i+1)
    if arr[i] > sub_max:
        return arr[i]
    else:
        return sub_max


print(my_max([5, 4, 3, 2, 9, 10]))  # Output: 10
```

---

## Cross-Language Notes

| Language | my\_sum               | my\_count             | my\_max               | Notes                                                                |
| -------- | --------------------- | --------------------- | --------------------- | -------------------------------------------------------------------- |
| Python   | O(n) time, O(n) space | O(n) time, O(n) space | O(n) time, O(n) space | Efficient version: no slicing, no costly pop(0)                      |
| C++      | O(n) time, O(n) space | O(n) time, O(n) space | O(n) time, O(n) space | Mirrors typical recursion with array indices/pointers                |
| Java     | O(n) time, O(n) space | O(n) time, O(n) space | O(n) time, O(n) space | Uses array indices, similar recursion stack                          |
| Go       | O(n) time, O(n) space | O(n) time, O(n) space | O(n) time, O(n) space | Slice indexing avoids element shifts                                 |
| Rust     | O(n) time, O(n) space | O(n) time, O(n) space | O(n) time, O(n) space | Slice borrowing ensures efficient recursion without extra allocation |

---

## Final Notes

* These optimized implementations are **cleaner and more efficient** than their `pop`/slicing counterparts.
* By using an **index parameter**, we eliminate unnecessary list copying and element shifting.
* Time complexity remains **O(n)**, and space complexity is **O(n)** due to recursion stack only.
* This approach closely matches how recursion is written in **C++, Java, Go, and Rust**, making the solutions more language-agnostic and scalable.