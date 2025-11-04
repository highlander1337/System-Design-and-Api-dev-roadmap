# C# Programming Essentials

## Introduction

This document provides an overview of essential programming concepts in
C#, focusing on Boolean logic, control structures, loops, methods, and
pseudocode.

## Boolean Logic and Control Structures

-   **Boolean Logic**: Fundamental for decision-making, involving
    operations like AND, OR, and NOT.

    **Example**:

    ``` csharp
    bool hasKey = true;
    bool doorLocked = false;

    if (hasKey && !doorLocked) {
        Console.WriteLine("You can open the door.");
    }
    ```

-   **Control Structures**: Includes if, else, and switch statements
    that guide program flow based on conditions.

    **Example**:

    ``` csharp
    int score = 85;

    if (score >= 90) {
        Console.WriteLine("Grade: A");
    } else if (score >= 80) {
        Console.WriteLine("Grade: B");
    } else {
        Console.WriteLine("Grade: C or below");
    }
    ```

## Using Loops for Repetition

-   **Loops**: Enable repetitive execution of code until a condition
    changes.

-   **For Loops**: Ideal for a specific number of iterations.

    **Example**:

    ``` csharp
    for (int i = 0; i < 5; i++) {
        Console.WriteLine("Iteration: " + i);
    }
    ```

-   **While Loops**: Continue executing as long as a condition is true,
    automating tasks and minimizing errors.

    **Example**:

    ``` csharp
    int count = 0;
    while (count < 5) {
        Console.WriteLine("Count: " + count);
        count++;
    }
    ```

## Organizing Code with Methods

-   **Methods**: Reusable blocks of code designed for specific tasks.

    **Example**:

    ``` csharp
    public static int Add(int a, int b) {
        return a + b;
    }

    // Usage
    int result = Add(5, 3);
    Console.WriteLine("Result: " + result);
    ```

## Planning with Pseudocode

-   **Pseudocode**: A planning tool that outlines program logic in plain
    language.

    **Example**:

        Initialize Car
        Check Gas Level
        If Gas > 0
            Increase Velocity
        Display Updated Status

## Conclusion

A solid understanding of these concepts is crucial for writing efficient
and maintainable programs in C#.
