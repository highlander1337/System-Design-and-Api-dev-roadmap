# Introduction to software testing

## 1. **Why We Test**

Software testing exists because:

* **Software is complex**, and developers make mistakes.
* Failures can have **massive financial**, **reputational**, and even **life-threatening** consequences (e.g., Yahoo data breach, British Airways outage, Therac-25 radiation accident).
* In 2016, software failures cost an estimated **$1.1 trillion** globally (Tricentis).

Testing helps ensure that software:

* **Performs as expected** (verification)
* **Meets user needs** (validation)

---

## 2. **Verification vs. Validation**

| Concept          | Guiding Question                        | Purpose                                         |
| ---------------- | --------------------------------------- | ----------------------------------------------- |
| **Verification** | “Are we building the software *right*?” | Confirms the product meets its **requirements** |
| **Validation**   | “Are we building the *right* product?”  | Confirms the product meets **user needs**       |

✅ Both are essential for quality.
Testing supports **both** verification and validation at multiple stages of the lifecycle.

---

## 3. **The Role of Testing Among Other Techniques**

Testing is one component of a larger **Verification & Validation (V&V)** toolkit:

| Technique                 | Description                                                 | When It’s Used    |
| ------------------------- | ----------------------------------------------------------- | ----------------- |
| **Inspections & Reviews** | Peer review of code/design                                  | Early development |
| **Static Analysis**       | Automated analysis for syntax, data flow, null derefs, etc. | Pre-runtime       |
| **Testing**               | Execute system to see if it behaves correctly               | Runtime           |
| **Runtime Verification**  | Monitors live systems for anomalies                         | Post-deployment   |

---

## 4. **Why Testing Is Irreplaceable**

Even though other techniques (like static analysis) are powerful, **testing is unique** because:

* It’s the **only way to check the entire system** — including compiler, OS, network, hardware, and third-party software.
* It’s the **most practical way** to assess **performance**, **integration**, and **user-facing behaviors**.
* It’s often **required for customer acceptance**.
* Tests can also **serve as documentation** in Agile and DevOps environments.

---

## 5. **The Challenge of Incompleteness**

Testing can never be exhaustive:

* The **input space** and **execution paths** are too large.
* The goal is not to test everything, but to test **effectively** — focusing on critical paths, representative cases, and risk-based coverage.

> 🎯 *Goal of this course:* Make testing **effective despite incompleteness.**

---

## 6. **The Testing Spectrum (Optimism vs. Pessimism)**

Whalen maps verification techniques on two axes:

#### **Horizontal axis:**

* **Optimistic techniques** → e.g., typical testing.

  * May say “it works” when it doesn’t.
  * Example: passing a few tests ≠ guaranteed correctness.
* **Pessimistic techniques** → e.g., Lint/static analyzers.

  * May say “it fails” when it doesn’t.
  * Example: false positives.

#### **Vertical axis:**

* **Simple properties** (e.g., type checking, syntax rules)
* **Complex properties** (e.g., functional correctness, security, performance)

---

## 7. **Examples of Techniques on This Spectrum**

| Level         | Technique                            | Nature                    | Notes                                             |
| ------------- | ------------------------------------ | ------------------------- | ------------------------------------------------- |
| Basic         | **Type Checking** (C, Java, Haskell) | Accurate, limited         | Detects simple well-formedness issues             |
| Intermediate  | **Static Analysis**                  | Pessimistic or unsound    | Finds deeper structural problems                  |
| Advanced      | **Testing (Manual/Automated)**       | Optimistic                | Checks specific behaviors                         |
| Advanced+     | **Coverage Testing**                 | More rigorous             | Ensures measurable test completeness              |
| Very Advanced | **Model Checking**                   | Exhaustive                | Possible only for small or well-specified systems |
| Expert        | **Theorem Proving**                  | Mathematical verification | Costly but powerful for critical software         |

---

## 8. **Key Takeaway: The Balanced Approach**

No single technique ensures correctness — software testing must be **combined** with static analysis, inspections, and design verification for a complete quality strategy.

---

## 9. **Testing in Practice — Objectives for the Backend Roadmap**

In the backend development roadmap, testing will serve to:

| Goal                            | Example                                                                                                |
| ------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Verification**                | Ensure API endpoints return correct responses, validate schemas and database constraints               |
| **Validation**                  | Check user workflows, data consistency, and integration with frontends or external systems             |
| **Automation**                  | Build CI/CD pipelines using tools like `pytest`, `unittest`, or `Playwright` for end-to-end validation |
| **Coverage & Metrics**          | Measure and improve code coverage (branch, line, path)                                                 |
| **Static Analysis Integration** | Use tools like `flake8`, `mypy`, and `bandit` to detect problems pre-runtime                           |

