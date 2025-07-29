# Big O notation

---

## 📘 What is Big O Notation?

**Big O Notation** is a mathematical way to describe the **efficiency** of an algorithm in terms of:

* **Time complexity** (how fast it runs)
* **Space complexity** (how much memory it uses)

It expresses how the runtime or memory usage grows **relative to the size of the input (n)**.

---

## 📏 Why Use Big O?

Big O ignores:

* Machine-specific behavior (CPU, RAM)
* Language-specific overhead

And focuses on:

* The **worst-case** performance
* **Scalability** of an algorithm as input size increases

This helps compare algorithms objectively.

---

## 🔍 Common Types of Big O Time Complexities

| Big O          | Name              | Description                                                         | Example                               |
| -------------- | ----------------- | ------------------------------------------------------------------- | ------------------------------------- |
| **O(1)**       | Constant Time     | Runtime does **not change** with input size                         | Accessing an array element            |
| **O(log n)**   | Logarithmic Time  | Runtime increases slowly as input size increases                    | Binary search                         |
| **O(n)**       | Linear Time       | Runtime increases proportionally with input                         | Loop through list                     |
| **O(n log n)** | Linearithmic Time | Combination of linear and logarithmic (common in efficient sorting) | Merge sort, quicksort (avg)           |
| **O(n²)**      | Quadratic Time    | Runtime grows **quadratically** with input (nested loops)           | Bubble sort, selection sort           |
| **O(2ⁿ)**      | Exponential Time  | Runtime doubles with each additional input                          | Recursive Fibonacci                   |
| **O(n!)**      | Factorial Time    | Runtime explodes with input size                                    | Solving permutations, TSP brute force |

---

## ⏱️ Time Complexity Examples

```python
# O(1) - Constant Time
def get_first_item(lst):
    return lst[0]

# O(n) - Linear Time
def print_all_items(lst):
    for item in lst:
        print(item)

# O(n²) - Quadratic Time
def print_all_pairs(lst):
    for item1 in lst:
        for item2 in lst:
            print(item1, item2)
```

---

## 💾 Space Complexity

Just like time, we use Big O for **memory usage**.

| Code Example                            | Space Complexity |
| --------------------------------------- | ---------------- |
| Use a few variables                     | O(1)             |
| Create a list of n elements             | O(n)             |
| Recursively store n calls on call stack | O(n)             |

---

## 🎯 Big O Notation Summary Table

| Notation       | Growth Rate Description                            | Performance Impact (large n)        |
| -------------- | -------------------------------------------------- | ----------------------------------- |
| **O(1)**       | Constant — best possible                           | Excellent                           |
| **O(log n)**   | Grows slowly even for big n                        | Great                               |
| **O(n)**       | Linear growth — manageable                         | Acceptable for moderate input sizes |
| **O(n log n)** | Log-linear, common in efficient sorting algorithms | Efficient                           |
| **O(n²)**      | Poor performance on large inputs                   | Inefficient                         |
| **O(2ⁿ)**      | Exponential — quickly becomes unusable             | Very bad                            |
| **O(n!)**      | Factorial — extreme explosion in computation       | Impractical                         |

---

## 💡 Tips

* Always consider **worst-case** when using Big O.
* Use **Big O** to guide decisions when working with large datasets.
* Know common complexities of data structures and algorithms:

  * Arrays: O(1) access, O(n) search
  * Hash tables: O(1) average insert/search
  * Binary search trees: O(log n) average search/insert
  * Graph traversals: BFS/DFS → O(V + E)

---
