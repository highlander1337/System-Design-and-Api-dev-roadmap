# 🏗️ End-to-End Example: Login Feature

We’ll build a **login function** that:

* Looks up a user in the database
* Verifies password
* Returns an authentication token

---

## 1️⃣ Step 1: Pseudocode (the logic blueprint)

```
FUNCTION login(username, password):
    user = FIND user IN database
    IF user does not exist:
        RETURN error "User not found"
    IF password is invalid:
        RETURN error "Invalid credentials"
    token = GENERATE authentication token
    RETURN token
```

👉 This is language-neutral. It just describes the **logic**.

---

## 2️⃣ Step 2: BDD Scenario (stakeholder view)

BDD describes the behavior from the **user’s perspective**.

```gherkin
Feature: User Login
  Scenario: Successful login
    Given a registered user "alice" with password "secret"
    When she logs in with correct credentials
    Then she should receive an authentication token

  Scenario: Login with wrong password
    Given a registered user "alice" with password "secret"
    When she logs in with password "wrong"
    Then she should receive an error "Invalid credentials"

  Scenario: Login with unregistered user
    When a user "bob" logs in with password "123"
    Then he should receive an error "User not found"
```

👉 Stakeholders can read this (no technical knowledge needed).

---

## 3️⃣ Step 3: TDD Unit Tests (developer view)

We take **each line of pseudocode** and make it into **unit tests**.

Example in Python (`pytest`):

```python
import pytest
from app.auth import login, create_user

def test_login_success_returns_token():
    create_user("alice", "secret")
    response = login("alice", "secret")
    assert "token" in response

def test_login_with_wrong_password_returns_error():
    create_user("alice", "secret")
    response = login("alice", "wrong")
    assert response == "Invalid credentials"

def test_login_with_unregistered_user_returns_error():
    response = login("bob", "123")
    assert response == "User not found"
```

👉 These tests are written **before implementation**.
At this stage, all tests will **fail** (Red phase of TDD).

---

## 4️⃣ Step 4: Implementation (making tests pass)

Now we implement the `login` function so tests turn **Green**.

### Python Example (minimal in-memory storage)

```python
import hashlib
import secrets

# simple in-memory "database"
users = {}

def create_user(username, password):
    # store hashed password for security
    users[username] = hashlib.sha256(password.encode()).hexdigest()

def login(username, password):
    # check if user exists
    if username not in users:
        return "User not found"

    # check password
    hashed = hashlib.sha256(password.encode()).hexdigest()
    if users[username] != hashed:
        return "Invalid credentials"

    # generate token
    token = secrets.token_hex(16)
    return {"token": token}
```

👉 Run the tests again → ✅ all pass.
We can now **Refactor** safely.

---

## 5️⃣ Step 5: BDD Step Definitions (glue code)

With a BDD framework (like `behave` in Python), we map the **Gherkin scenarios** to real code.

```python
from behave import given, when, then
from app.auth import create_user, login

@given('a registered user "{username}" with password "{password}"')
def step_impl(context, username, password):
    create_user(username, password)

@when('she logs in with correct credentials')
def step_impl(context):
    context.response = login("alice", "secret")

@when('she logs in with password "{password}"')
def step_impl(context, password):
    context.response = login("alice", password)

@when('a user "{username}" logs in with password "{password}"')
def step_impl(context, username, password):
    context.response = login(username, password)

@then('she should receive an authentication token')
@then('he should receive an authentication token')
def step_impl(context):
    assert "token" in context.response

@then('she should receive an error "{message}"')
@then('he should receive an error "{message}"')
def step_impl(context, message):
    assert context.response == message
```

👉 Now the **BDD scenarios run as automated tests**, validating both business rules and backend logic.

---

## 6️⃣ End-to-End Flow Recap

1. **Pseudocode** → defines the logic in plain language.
2. **BDD scenarios** → capture stakeholder expectations.
3. **TDD unit tests** → enforce logic correctness at low-level.
4. **Implementation** → make tests pass.
5. **BDD automation** → ensures business rules are continuously validated.

---

✅ With this flow, we’ve gone **from idea → stakeholder scenarios → passing backend code** in a **traceable, testable way**.
This is exactly how professional teams keep code maintainable and aligned with requirements.
