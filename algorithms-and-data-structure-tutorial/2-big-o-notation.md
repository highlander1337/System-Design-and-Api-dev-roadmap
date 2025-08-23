# Big O Notation

---

## 📘 What is Big O Notation?

**Big O Notation** is a mathematical way to describe the **efficiency** of an algorithm in terms of:

* **Time complexity** (how fast it runs)
* **Space complexity** (how much memory it uses)

It expresses how the runtime or memory usage grows **relative to the size of the input (n)**.

Big O doesn’t measure the exact runtime but rather the **growth rate** of the algorithm as inputs get larger.

---

## 📏 Why Use Big O?

Big O ignores:

* Machine-specific behavior (CPU, RAM)
* Language-specific overhead

And focuses on:

* The **worst-case** performance (upper bound)
* **Scalability** of an algorithm as input size increases

This helps compare algorithms **objectively**, even across different computers and programming languages.

---

## 🔍 Common Types of Big O Time Complexities

| Big O          | Name              | Description                                                         | Example                               |
| -------------- | ----------------- | ------------------------------------------------------------------- | ------------------------------------- |
| **O(1)**       | Constant Time     | Runtime does **not change** with input size                         | Accessing an array element            |
| **O(log n)**   | Logarithmic Time  | Runtime increases very slowly as input size grows                   | Binary search                         |
| **O(n)**       | Linear Time       | Runtime increases proportionally with input                         | Loop through list                     |
| **O(n log n)** | Linearithmic Time | Combination of linear and logarithmic (common in efficient sorting) | Merge sort, quicksort (average case)  |
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

## 📐 Divide and Conquer & Base Cases

Many efficient algorithms use a **Divide and Conquer** strategy:

1. **Divide** the problem into smaller subproblems.
2. **Conquer** each subproblem recursively.
3. **Combine** the solutions.

For recursion, the **base case** is the smallest version of the problem that can be solved directly, without further recursion.
Examples:

* In **binary search**, base case = list is empty or one element.
* In **quicksort**, base case = array of size 0 or 1 (already sorted).

Recognizing a **clear base case** prevents infinite recursion and anchors the algorithm.

---

## ⚖️ Average vs. Worst Case

* Some algorithms have very different **average-case** and **worst-case** behavior.
* Example:
  *Quicksort* is **O(n log n)** on average, but in the **worst case** (bad pivot every time), it degrades to **O(n²)**.
* Mergesort is always **O(n log n)** (more predictable).

This distinction matters when choosing algorithms in practice.

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

| Notation       | Growth Rate Description                      | Performance Impact (large n)        |
| -------------- | -------------------------------------------- | ----------------------------------- |
| **O(1)**       | Constant — best possible                     | Excellent                           |
| **O(log n)**   | Grows very slowly, even for large n          | Great                               |
| **O(n)**       | Linear growth — manageable                   | Acceptable for moderate input sizes |
| **O(n log n)** | Common in efficient sorting algorithms       | Efficient                           |
| **O(n²)**      | Poor performance on large inputs             | Inefficient                         |
| **O(2ⁿ)**      | Exponential — quickly becomes unusable       | Very bad                            |
| **O(n!)**      | Factorial — extreme explosion in computation | Impractical                         |

---

## ⚡ Practical Considerations

* **Constants matter in practice.**
  Two algorithms with the same Big O may perform differently — e.g., Quicksort is often faster than Mergesort because of smaller hidden constants and better use of memory caches.

* **Orders of growth dominate constants.**
  Even if O(n) has a smaller constant than O(log n), for very large `n`, O(log n) will almost always be better.

* **Think about the real input size.**
  For small datasets, simpler algorithms (like O(n²) bubble sort) can sometimes outperform more complex ones (like O(n log n) mergesort) because overhead is smaller.

---

## 💡 Tips

* Always consider **worst-case** when using Big O.
* Look at **average-case** for algorithms like Quicksort where behavior varies.
* Use **Big O** to guide decisions when working with large datasets.
* Know common complexities of data structures and algorithms:

  * Arrays: O(1) access, O(n) search
  * Hash tables: O(1) average insert/search
  * Binary search trees: O(log n) average search/insert
  * Graph traversals: BFS/DFS → O(V + E)
