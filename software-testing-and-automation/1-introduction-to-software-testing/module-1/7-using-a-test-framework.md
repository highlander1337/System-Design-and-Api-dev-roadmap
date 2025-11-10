# 🧪 Automated Testing Frameworks in Practice

### Cross-Language Demonstration and Analysis

Testing frameworks allow developers to **automate code validation** and **continuously verify correctness** across code changes.
This section extends the triangle example shown with **JUnit (Java)** and re-implements it using **Python (pytest)**, **C# (xUnit/NUnit)**, and **C++ (GoogleTest)** — demonstrating how consistent testing principles manifest in different ecosystems.

---

## 🟡 1. Java Example — *JUnit 5 in Eclipse*

### Code Example

```java
// Demo.java
public class Demo {
    public static boolean isTriangle(int a, int b, int c) {
        // Corrected implementation
        return (a + b > c) && (a + c > b) && (b + c > a);
    }
}
```

```java
// DemoTest.java
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class DemoTest {

    @Test
    void test_isTriangle_3_4_5() {
        assertTrue(Demo.isTriangle(3, 4, 5));
    }

    @Test
    void test_isTriangle_invalid_5_7_13() {
        assertFalse(Demo.isTriangle(5, 7, 13));
    }

    @Test
    void test_isTriangle_reordered() {
        assertTrue(Demo.isTriangle(5, 12, 13));
        assertTrue(Demo.isTriangle(12, 13, 5));
    }
}
```

### Technical Benefits

✅ Built-in IDE support (Eclipse, IntelliJ).
✅ Fast feedback with clear “green/red bar” visualization.
✅ Supports **annotations (@Test, @BeforeAll, @AfterEach)** for setup/teardown.
✅ Integrates seamlessly into **Maven/Gradle CI pipelines**.
✅ Encourages modular, decomposed code that’s easier to test.

### Common Pitfalls

⚠️ **Overusing shared state** — each test should be isolated.
⚠️ **Ignoring edge cases** (e.g., zero or negative inputs).
⚠️ **Testing through main()** — avoid console-bound I/O in tests.
⚠️ **Assuming order dependence** — JUnit runs tests independently and may reorder them.

---

## 🟢 2. Python Example — *pytest*

### Code Example

```python
# demo.py
def is_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)
```

```python
# test_demo.py
import pytest
from demo import is_triangle

@pytest.mark.parametrize("a,b,c,expected", [
    (3, 4, 5, True),
    (5, 7, 13, False),
    (5, 12, 13, True),
    (1, 2, 3, False),
])
def test_is_triangle(a, b, c, expected):
    assert is_triangle(a, b, c) == expected
```

### Technical Benefits

✅ **Parametrization** reduces code duplication — one function tests many cases.
✅ Works naturally with **assert statements** (no framework-specific syntax).
✅ Integrates with **pytest-cov** for coverage and **pytest-xdist** for parallel execution.
✅ Simplifies **setup/teardown** using `@pytest.fixture`.
✅ Extremely fast feedback cycle; ideal for TDD and CI/CD.

### Common Pitfalls

⚠️ Forgetting to include the `test_` prefix — pytest won’t discover the test.
⚠️ Over-mocking — mocks should only replace *slow or external* dependencies.
⚠️ Misusing fixtures — global fixtures can create unwanted side effects.
⚠️ Not separating *unit* and *integration* tests — slows test suites unnecessarily.

---

## 🔵 3. C# Example — *xUnit / NUnit*

### Code Example (xUnit)

```csharp
// Demo.cs
public class Demo {
    public static bool IsTriangle(int a, int b, int c) {
        return (a + b > c) && (a + c > b) && (b + c > a);
    }
}
```

```csharp
// DemoTests.cs
using Xunit;

public class DemoTests {
    [Theory]
    [InlineData(3, 4, 5, true)]
    [InlineData(5, 7, 13, false)]
    [InlineData(12, 13, 5, true)]
    public void IsTriangle_Validations_ReturnsExpected(int a, int b, int c, bool expected) {
        Assert.Equal(expected, Demo.IsTriangle(a, b, c));
    }
}
```

### Technical Benefits

✅ **[Theory]** and **[InlineData]** support parameterized testing.
✅ xUnit runs each test in isolation — perfect for parallel CI.
✅ Tight integration with **Visual Studio Test Explorer** and **.NET CLI** (`dotnet test`).
✅ NUnit offers similar structure with attributes like `[TestCase]` and `[SetUp]`.

### Common Pitfalls

⚠️ Confusing **TestClass lifecycle** — `[SetUp]`, `[TearDown]` differ between xUnit and NUnit.
⚠️ Using static/shared mutable state — breaks test isolation.
⚠️ Overusing mocks for simple logic (prefer real function calls).
⚠️ Forgetting CI integration with `dotnet test --collect:"Code Coverage"`.

---

## 🔴 4. C++ Example — *GoogleTest (gtest)*

### Code Example

```cpp
// demo.cpp
bool isTriangle(int a, int b, int c) {
    return (a + b > c) && (a + c > b) && (b + c > a);
}
```

```cpp
// test_demo.cpp
#include "gtest/gtest.h"
#include "demo.cpp" // typically you'd include a header instead

TEST(IsTriangleTest, ValidTriangles) {
    EXPECT_TRUE(isTriangle(3, 4, 5));
    EXPECT_TRUE(isTriangle(5, 12, 13));
}

TEST(IsTriangleTest, InvalidTriangles) {
    EXPECT_FALSE(isTriangle(5, 7, 13));
    EXPECT_FALSE(isTriangle(1, 2, 3));
}
```

### Running Tests

```bash
g++ demo.cpp test_demo.cpp -lgtest -lpthread -o tests
./tests
```

### Technical Benefits

✅ **Fast native execution**, ideal for embedded or performance-critical systems.
✅ Strong **assertion macros** (`EXPECT_EQ`, `EXPECT_TRUE`, etc.) with detailed output.
✅ Built-in **fixtures** (`TEST_F`) and **parameterized tests** (`TEST_P`).
✅ Excellent CI integration (CMake + GitHub Actions or Jenkins).

### Common Pitfalls

⚠️ Forgetting to link with pthread (`-lpthread`) — required on Linux.
⚠️ Including source instead of headers — breaks modularity.
⚠️ Limited runtime mocking without additional libraries (e.g., GoogleMock).
⚠️ Misusing `ASSERT_*` vs. `EXPECT_*` — the former halts a test immediately.

---

## ⚙️ Comparative Summary

| Language   | Framework   | Strengths                                                 | Common Pitfalls                                 |
| ---------- | ----------- | --------------------------------------------------------- | ----------------------------------------------- |
| **Java**   | JUnit 5     | Mature ecosystem, annotation-based setup, strong CI tools | Test order independence, console I/O complexity |
| **Python** | pytest      | Simple syntax, parameterization, high developer velocity  | Naming conventions, fixture misuse              |
| **C#**     | xUnit/NUnit | IDE integration, parameterized tests, parallel-safe       | Test lifecycle confusion, static state issues   |
| **C++**    | GoogleTest  | Native performance, expressive assertions, flexible setup | Linking issues, limited mocking tools           |

---

## 🧠 Cross-Language Observations

1. **Common Architectural Benefit:**

   * All frameworks encourage *functional decomposition* — breaking monolithic code into testable units.

2. **Automation & CI Integration:**

   * All tools integrate easily into CI/CD pipelines (GitHub Actions, Jenkins, Azure DevOps).
   * Re-running regression suites is as easy as a single command (`pytest`, `mvn test`, `dotnet test`, `ctest`).

3. **Shift-Left Testing:**

   * Earlier adoption in the SDLC (during design/implementation) reduces cost of defect discovery.

4. **Culture of Confidence:**

   * Automated test feedback creates *confidence for refactoring* — enabling agile iteration and code evolution.

---

## 🧩 Example CI/CD Integration

| Platform                     | Command                                    | Description                                      |
| ---------------------------- | ------------------------------------------ | ------------------------------------------------ |
| **Python (pytest)**          | `pytest --maxfail=1 --disable-warnings -q` | Fast feedback loop                               |
| **Java (JUnit + Maven)**     | `mvn test`                                 | Standard Maven goal for automated test execution |
| **C# (.NET)**                | `dotnet test`                              | Integrates with Visual Studio and Azure DevOps   |
| **C++ (CMake + GoogleTest)** | `ctest --output-on-failure`                | Runs all compiled tests after build              |

Each ecosystem supports **continuous testing**, ensuring that quality gates run automatically before merges or deployments.

---

## 🧠 Summary: The Engineering Value of Test Frameworks

| Value                          | Description                                                                                |
| ------------------------------ | ------------------------------------------------------------------------------------------ |
| **Repeatability**              | Automated tests remove human error and ensure consistency across runs.                     |
| **Scalability**                | Thousands of tests can run in seconds — ideal for regression testing.                      |
| **Isolation**                  | Unit tests promote modular design and reduce coupling.                                     |
| **Confidence in Change**       | Developers can safely refactor knowing that test suites validate functionality.            |
| **Cross-Language Portability** | Core testing principles remain consistent — input, output, and expected result validation. |

> **Automated testing frameworks transform testing from a manual burden into a continuous engineering discipline.**
> No matter the language — Java, Python, C#, or C++ — the goal remains the same:
> *Build software that proves its own correctness.*
