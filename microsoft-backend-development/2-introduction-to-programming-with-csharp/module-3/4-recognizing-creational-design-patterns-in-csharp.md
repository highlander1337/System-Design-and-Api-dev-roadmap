# 🧱 **Recognizing Creational Design Patterns in C#**

## **1. Singleton Pattern**

> Ensures only one instance of a class exists and provides global access to it.

### 🔍 **How to recognize it**

Look for:

* A **private constructor** (prevents external instantiation).
* A **static property or method** (usually named `Instance` or `GetInstance`).
* A **static field** holding the single instance.
* Optional: a **lock** or **Lazy<T>** usage for thread-safety.

### ✅ **Typical C# Example**

```csharp
public class ConfigurationManager
{
    private static ConfigurationManager _instance;
    private static readonly object _lock = new object();

    private ConfigurationManager() { }

    public static ConfigurationManager Instance
    {
        get
        {
            lock (_lock)
            {
                return _instance ?? (_instance = new ConfigurationManager());
            }
        }
    }

    public string GetSetting(string key) => "SomeValue";
}
```

### 💡 **Recognition clues**

* `private` constructor → can’t `new` from outside.
* Accessed via `ClassName.Instance`.
* Thread-safety patterns or `Lazy<T>` → `new Lazy<ClassName>(() => new ClassName())`.

---

## **2. Factory Method Pattern**

> Defines an interface for creating objects but lets subclasses decide which class to instantiate.

### 🔍 **How to recognize it**

Look for:

* A **method** that returns an interface or abstract type (`IFoo`, `IProduct`).
* Conditional logic or lookup determining which concrete class to return.
* Call sites that depend on the **factory method**, not `new`.

### ✅ **Typical C# Example**

```csharp
public interface INotification { void Send(string msg); }

public class EmailNotification : INotification { public void Send(string msg) { } }
public class SmsNotification : INotification { public void Send(string msg) { } }

public class NotificationFactory
{
    public INotification Create(string type)
    {
        if (type == "Email") return new EmailNotification();
        if (type == "SMS") return new SmsNotification();
        throw new ArgumentException("Invalid type");
    }
}
```

### 💡 **Recognition clues**

* Return type is **interface or abstract class**.
* Method name often starts with `Create` or `Build`.
* Conditional (`if/else`, `switch`, dictionary lookup) decides type.
* **No `new`** statements outside the factory.

---

## **3. Abstract Factory Pattern**

> Provides an interface to create families of related or dependent objects without specifying concrete classes.

### 🔍 **How to recognize it**

Look for:

* A **factory interface** with multiple related creation methods.
* Several **concrete factories** implementing the same interface.
* The **client** depends only on the abstract factory, not on the products or their implementations.

### ✅ **Typical C# Example**

```csharp
public interface IUIFactory
{
    IButton CreateButton();
    ITextBox CreateTextBox();
}

public class WindowsUIFactory : IUIFactory
{
    public IButton CreateButton() => new WindowsButton();
    public ITextBox CreateTextBox() => new WindowsTextBox();
}

public class MacUIFactory : IUIFactory
{
    public IButton CreateButton() => new MacButton();
    public ITextBox CreateTextBox() => new MacTextBox();
}
```

### 💡 **Recognition clues**

* Multiple creation methods grouped by family.
* Same **interface** for all factories.
* The client never mentions concrete classes like `WindowsButton` — only `IUIFactory`.

---

## **4. Builder Pattern**

> Separates the construction of a complex object from its representation.

### 🔍 **How to recognize it**

Look for:

* A **Builder class** with step-by-step methods (like `SetName`, `AddPart`, `WithX`).
* A **`Build()`** or **`GetResult()`** method at the end.
* Often used with **fluent interfaces**.
* The **Director** (or the client) coordinates building.

### ✅ **Typical C# Example**

```csharp
public class Report
{
    public string Header { get; set; }
    public string Body { get; set; }
    public string Footer { get; set; }
}

public class ReportBuilder
{
    private readonly Report _report = new Report();

    public ReportBuilder SetHeader(string header) { _report.Header = header; return this; }
    public ReportBuilder SetBody(string body) { _report.Body = body; return this; }
    public ReportBuilder SetFooter(string footer) { _report.Footer = footer; return this; }
    public Report Build() => _report;
}
```

### 💡 **Recognition clues**

* Method chaining (fluent interface) — `builder.WithX().WithY().Build()`.
* Final method `Build()` or `GetResult()`.
* Object under construction often has **many optional parts**.

---

## **5. Prototype Pattern**

> Creates new objects by copying existing ones (cloning).

### 🔍 **How to recognize it**

Look for:

* A class that implements `ICloneable` or defines a `Clone()` method.
* New instances are **created from existing ones**, not via `new`.
* Deep vs. shallow copy logic.

### ✅ **Typical C# Example**

```csharp
public class Document : ICloneable
{
    public string Content { get; set; }
    public object Clone()
    {
        return this.MemberwiseClone(); // shallow copy
    }
}
```

### 💡 **Recognition clues**

* Presence of `Clone()` or `Copy()` methods.
* Calls to `MemberwiseClone()` or serialization-based copy.
* Object creation is **based on duplication**, not construction.

---

# 🧠 **Quick Recognition Summary**

| Pattern              | Core Intent                        | C# Clues                                       | Typical Code Feature                           |
| -------------------- | ---------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| **Singleton**        | Ensure only one instance           | Private constructor, static `Instance`         | `private static` instance + thread-safety lock |
| **Factory Method**   | Delegate object creation           | Returns `interface`, uses `if`/`switch`        | Method named `CreateSomething()`               |
| **Abstract Factory** | Create families of related objects | Multiple `CreateX()` methods on same interface | Factory interface + multiple implementations   |
| **Builder**          | Step-by-step object construction   | `WithX()` / `SetX()` chain + `Build()`         | Fluent API returning the builder               |
| **Prototype**        | Clone existing object              | Implements `ICloneable`, `Clone()`             | Calls to `MemberwiseClone()`                   |

---

# 🔍 **Advanced Recognition Tip: Check “Where the `new` Happens”**

If you’re analyzing code and want to detect a creational pattern:

1. **Find where `new` keywords appear**.

   * If `new` is used only inside factories → **Factory Method** or **Abstract Factory**.
   * If `new` is used inside a static property → **Singleton**.
   * If `new` is used step-by-step with chained methods → **Builder**.
   * If `new` isn’t used at all and objects are copied → **Prototype**.

2. **Check who owns the creation responsibility**.

   * If a dedicated class exists just for creation → likely a **Factory** or **Builder**.
   * If creation is centralized and hidden from the client → **Creational Pattern Detected** ✅.

---

# ⚙️ **In Practice: Applying This When Reading Code**

When reading C# backend or enterprise codebases:

* Look for **factories** under folders like `Factories`, `Builders`, or `Providers`.
* Scan for **static accessors** or **private constructors** → `Singleton`.
* Identify **fluent APIs** or **configuration chaining** → `Builder`.
* Search for **clone-based logic** or object duplication → `Prototype`.
* Check if factories produce **multiple related objects** → `Abstract Factory`.

---

# ✅ **In Summary**

Creational patterns are all about *where and how objects come to life*:

| Pattern          | Creation Source           | Variation           | Flexibility Level |
| ---------------- | ------------------------- | ------------------- | ----------------- |
| Singleton        | Class itself (1 instance) | None                | 🔒 Low            |
| Factory Method   | Subclass or conditional   | Type-based          | 🟡 Medium         |
| Abstract Factory | Factory family            | Context-based       | 🟢 High           |
| Builder          | Separate builder object   | Configuration-based | 🟢 High           |
| Prototype        | Existing object clone     | Data-based          | 🟢 High           |

> 🧠 **Rule of Thumb:**
> If you see a `new` keyword hidden behind a method, you’re likely looking at a **creational pattern**.
