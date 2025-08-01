
# Even or odd number

Create a flowchart and pseudocode for a simple program that checks if a number is even or odd. If the number is even, the program should print "Even number"; otherwise, it should print "Odd number".

## Problem definition

The user must enter a number and the code will check if the number is even or odd, the number must be an integer and it must check if its really a number before moving any further.

### ✅ Enhanced Problem Definition

#### Problem Statement

Design a program that determines whether a user-provided input is an even or odd number. The program must validate that the input is a valid integer before attempting to evaluate its parity (even or odd). If the input is not a valid integer, the program should display an appropriate error message and terminate gracefully. If the input is valid, the program should check the number’s parity and display either "Even number" or "Odd number".

#### Functional Requirements

1. **Input Handling:**

   * Prompt the user to enter a value.
   * Validate that the input is a number.
   * Check that the number is an **integer** (i.e., no decimals).

2. **Parity Check:**

   * If the number is divisible by 2 (i.e., `number % 2 == 0`), print `"Even number"`.
   * Otherwise, print `"Odd number"`.

3. **Error Handling:**

   * If the input is not numeric or not an integer, print `"Invalid input. Please enter an integer."`.

### 🧠 Thought Process Behind the Improvements

### 1. **Clarity of Intent**

* Original: “The user must enter a number…”

  * ✅ Now: Specifies *what kind* of number (integer), and *what to do* if the input is invalid.
  * 🔍 Why: This eliminates ambiguity. A “number” could be a float, complex number, or a string of digits — clarity helps prevent incorrect assumptions during implementation.

#### 2. **Separation of Concerns**

* Split into input validation and parity check.

  * 🔍 Why: This reflects how we should structure the code: **input → validation → logic → output**. It also makes it easier to debug and extend later.

#### 3. **Handling Edge Cases**

* Included an error-handling path.

  * 🔍 Why: Beginner-level exercises often overlook how the program should respond to bad input. Thinking about what can go wrong leads to more robust programs.

#### 4. **Action-Oriented Language**

* Rephrased into active steps (e.g., “Prompt the user,” “Validate,” “Check,” “Print”).

  * 🔍 Why: This makes the problem definition more actionable and maps more clearly to pseudocode and implementation.

### 🧪 Learning Takeaway: How to Improve Your Own Problem Definitions

Here’s a **step-by-step checklist** for writing better problem definitions:

| Step                   | Question to Ask                                               | Goal                                   |
| ---------------------- | ------------------------------------------------------------- | -------------------------------------- |
| 1. Clarify the Goal    | What is the **end result** the user wants?                    | Clear statement of desired output      |
| 2. Define the Input    | What kind of input is expected? What format? Any constraints? | Prevent ambiguity                      |
| 3. Handle Errors       | What if the user gives unexpected input?                      | Improve robustness                     |
| 4. Break It Down       | Can the task be divided into logical steps or phases?         | Aligns problem with code structure     |
| 5. Generalize Slightly | Will the logic hold for all valid inputs?                     | Prepare for scalability or reusability |

## Identify Key Processes

* Ask the user to input a number
* Validate user input
* Check if it is odd or even if the number is valid

### ✅ Enhanced Key Processes (with Explanations)

1. Prompt user to enter an integer.
2. Store the input as a string.
3. Validate if the string represents a valid integer.
4. If invalid, print an error and terminate.
5. If valid, convert the string to an integer.
6. Check if the integer is divisible by 2:

   * If yes, print “Even number”.
   * If not, print “Odd number”.

#### 1. **Prompt for Input**

* **What it means:** Display a message asking the user to enter a number.
* **Why it matters:** The first interaction point — user guidance is key. A vague prompt like “Enter a number” could confuse users if you actually require an integer.
* **Improved version:**

  * *“Display a prompt requesting the user to enter an integer.”*

#### 2. **Receive and Store Input**

* **What it means:** Capture the raw input entered by the user.
* **Why it matters:** Most programming languages treat input as a string. Recognizing this helps plan for type checking or conversion.
* **Improved version:**

  * *“Store the user input as a string for further validation.”*

#### 3. **Validate Input**

* **What it means:** Check that the input is a valid **integer** (not empty, not a float, not letters, etc.).
* **Why it matters:** Good validation prevents your program from crashing or behaving unexpectedly.
* **Improved version:**

  * *“Check if the input string represents a valid integer. If not, display an error message and exit.”*

#### 4. **Convert Input**

* **What it means:** After validation, convert the input from string to integer.
* **Why it matters:** You can't use `%` modulo operator on a string. Type conversion is essential for logic execution.
* **Improved version:**

  * *“Convert the validated input string to an integer for processing.”*

#### 5. **Determine Parity (Even or Odd)**

* **What it means:** Use modulo operation to check divisibility by 2.
* **Why it matters:** The core logic. Clearly stating the condition used helps ensure correctness.
* **Improved version:**

  * *“If the number modulo 2 equals 0, classify it as even; else, classify it as odd.”*

#### 6. **Display Result**

* **What it means:** Output “Even number” or “Odd number” based on the check.
* **Why it matters:** User feedback is the final goal. Be explicit in your output format.
* **Improved version:**

  * *“Print ‘Even number’ or ‘Odd number’ based on the result of the parity check.”*

## Draw the Flowchart

``` mermaid
flowchart TD

Start([Start])
Input[/Enter an <br>integer number/]
Storage[Store user input<br> as a string]
Validate{Is input valid?}
ErrorMessage[/Error message/]
Parity{Is number <br> Odd ?}
DisplayOdd[/The number is Odd/]
DisplayEven[/The number is Even/]
End([End])

Start --> Input
Input --> Storage
Storage --> Validate
Validate -- Yes --> Parity
Validate -- No --> ErrorMessage --> End
Parity -- Yes --> DisplayOdd --> End
Parity -- No --> DisplayEven --> End

```

## Transition to pseudocode

* Start (flowchart) translate to start(pseudocode) initiate the function process

* Enter an integer number (flowchart) translate to Allow user to enter a integer number

* Store user input as a string (flowchart) translate to Create a string variable and set to user input

* Is input valid? (flowchart) translate to If attempt to convert the string into a integer succed

* Is number Odd? (flowchart) translate to If module operand (number % 2) not equal to zero

* The number is Odd (flowchart) translate to Display: "The number is Odd"

* The number is Even (flowchart) translate to Display: "The number is Even"

* Error message (flowchart) translate to Display: "Please, provide only integer numbers"

## Pseudocode

``` none

function checkOddOrEven():
    # Start
    begin

    # Prompt user to enter an integer
    display "Enter an integer number: "
    
    # Create a string variable and store input
    userInput = get input as string

    # Attempt to convert input to integer
    try:
        number = convert userInput to integer

        # Check if number is odd
        if number % 2 != 0 then
            display "The number is Odd"
        else
            display "The number is Even"

    catch ConversionError:
        # If conversion fails, input is not an integer
        display "Please, provide only integer numbers"

    # End
end function

```
