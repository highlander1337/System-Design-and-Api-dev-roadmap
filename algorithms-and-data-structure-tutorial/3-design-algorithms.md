# Design and build algorithms

To build a good algorithm, you should follow a structured, step-by-step approach that ensures your solution is **correct**, **efficient**, and **maintainable**. Below are the **essential steps**:

---

## ✅ Steps to Build a Good Algorithm

### 1. **Understand the Problem**

* **Clarify the input and output** requirements.
* Identify constraints (time limits, memory limits, valid input ranges).
* Ask questions if anything is ambiguous.

> *Example*: “Find the index of an element in a sorted list.”

---

### 2. **Analyze Examples**

* Work through **small test cases** manually.
* Understand edge cases (empty input, duplicates, invalid values).
* Use these to shape your thinking and test later.

> *Example*: For input `[1, 3, 5, 7]` and target `5`, the index should be `2`.

---

### 3. **Break the Problem Into Sub-Problems**

* Use **decomposition** to split into smaller tasks.
* Focus on parts you can solve easily.

> *Example*: "First, check the midpoint; then eliminate half the list."

---

### 4. **Choose the Right Data Structures and Approach**

* Decide on the best algorithmic **paradigm**:

  * Brute force
  * Divide and conquer
  * Greedy
  * Recursion
  * Dynamic programming
  * Backtracking

* Pick the right **data structures**:

  * Arrays/lists, hash maps, stacks, queues, trees, graphs, etc.

> *Example*: Use **binary search** for a sorted array to get O(log n) time.

---

### 5. **Design the Algorithm Step-by-Step**

* Write **pseudocode** or outline steps logically.
* Think about:

  * What happens at each step?
  * When does it stop?
  * What’s the result?

> *Pseudocode Example*:

```text
while start <= end:
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    else if arr[mid] < target:
        start = mid + 1
    else:
        end = mid - 1
```

---

### 6. **Analyze Time and Space Complexity**

* Use **Big O Notation** to express performance:

  * Time complexity: How does time scale with input?
  * Space complexity: How much memory is used?

> *Example*: Binary search → Time: O(log n), Space: O(1)

---

### 7. **Implement the Algorithm**

* Write clean, readable code.
* Follow best practices: naming, formatting, modularity.

> Use functions, avoid code repetition, and add comments for clarity.

---

### 8. **Test with Multiple Cases**

* Test against:

  * Normal cases
  * Edge cases
  * Large inputs
  * Invalid inputs (if applicable)

> *Example*: Empty input, input with one item, or input with duplicates.

---

### 9. **Optimize If Necessary**

* Can you reduce time or space?
* Avoid redundant calculations (use memoization if needed).
* Eliminate unnecessary loops or operations.

> *Example*: Replace nested loops (O(n²)) with hashing (O(n)) if possible.

---

### 10. **Document and Refactor**

* Add **comments** to explain key logic.
* Refactor to improve readability and maintainability.
* Keep functions short and focused.

---

## 🧠 Final Thought

> “A good algorithm is not just one that works, but one that works **well**, is **easy to understand**, and can be **adapted or improved** when needed.”
