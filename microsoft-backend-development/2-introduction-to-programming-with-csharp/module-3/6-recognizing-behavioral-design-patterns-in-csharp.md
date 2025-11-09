# 🧠 **Recognizing Behavioral Design Patterns in C#**

---

## **1. Chain of Responsibility**

> Passes a request along a chain of handlers until one handles it.

### 🔍 **How to Recognize It**

* Multiple handler classes share a **common interface** (e.g., `IHandler`).
* Each handler has a **reference to the next handler**.
* Requests are **passed along the chain** until handled.
* Often used for **middleware**, **validation**, or **authorization**.

### ✅ **Typical C# Example**

```csharp
public interface IHandler
{
    void Handle(string request);
}

public class AuthHandler : IHandler
{
    private readonly IHandler _next;
    public AuthHandler(IHandler next) => _next = next;

    public void Handle(string request)
    {
        if (request.Contains("Auth")) Console.WriteLine("AuthHandler processed.");
        else _next?.Handle(request);
    }
}

public class LogHandler : IHandler
{
    private readonly IHandler _next;
    public LogHandler(IHandler next) => _next = next;

    public void Handle(string request)
    {
        Console.WriteLine("Logging request...");
        _next?.Handle(request);
    }
}
```

### 💡 **Recognition Clues**

* A linked chain of handlers (`_next` field).
* Calls `_next?.Handle(request)` or similar.
* Used heavily in ASP.NET Core middleware or validation pipelines.

---

## **2. Command Pattern**

> Encapsulates a request as an object, allowing it to be queued, undone, or logged.

### 🔍 **How to Recognize It**

* Commands implement a **common interface** (e.g., `ICommand`).
* A **Receiver** performs the actual work.
* An **Invoker** triggers the command.
* Commands are often **queued**, **stored**, or **replayed**.

### ✅ **Typical C# Example**

```csharp
public interface ICommand
{
    void Execute();
}

public class CreateOrderCommand : ICommand
{
    private readonly string _orderId;
    public CreateOrderCommand(string orderId) => _orderId = orderId;
    public void Execute() => Console.WriteLine("Creating order " + _orderId);
}

public class CommandInvoker
{
    private readonly Queue<ICommand> _commands = new Queue<ICommand>();
    public void AddCommand(ICommand command) => _commands.Enqueue(command);
    public void ProcessAll()
    {
        while (_commands.Count > 0)
            _commands.Dequeue().Execute();
    }
}
```

### 💡 **Recognition Clues**

* Each action is represented as an **object**.
* Contains an `Execute()` or `Run()` method.
* Often used in **CQRS**, **task queues**, **macro recording**, or **undo systems**.

---

## **3. Interpreter Pattern**

> Defines a grammar and an interpreter that uses it to interpret sentences in that language.

### 🔍 **How to Recognize It**

* A class hierarchy representing grammar rules.
* An `Interpret(Context)` method in multiple classes.
* Frequently used for **expression trees**, **rule engines**, or **DSLs**.

### ✅ **Typical C# Example**

```csharp
public interface IExpression
{
    int Interpret();
}

public class Number : IExpression
{
    private readonly int _value;
    public Number(int value) => _value = value;
    public int Interpret() => _value;
}

public class Add : IExpression
{
    private readonly IExpression _left, _right;
    public Add(IExpression left, IExpression right)
    {
        _left = left; _right = right;
    }
    public int Interpret() => _left.Interpret() + _right.Interpret();
}
```

### 💡 **Recognition Clues**

* Classes named after grammar constructs (`Add`, `Subtract`, `Variable`).
* Methods like `Interpret(Context)` or `Evaluate()`.
* Often used in **scripting**, **rule-based engines**, or **query languages**.

---

## **4. Iterator Pattern**

> Provides a way to sequentially access elements in a collection without exposing its structure.

### 🔍 **How to Recognize It**

* A separate **iterator class** or `IEnumerator<T>` implementation.
* Methods like `MoveNext()`, `Current`, and `Reset()`.
* Often custom iterators over internal data structures.

### ✅ **Typical C# Example**

```csharp
public class CustomCollection : IEnumerable<int>
{
    private int[] _numbers = { 1, 2, 3, 4 };

    public IEnumerator<int> GetEnumerator()
    {
        foreach (var n in _numbers)
            yield return n;
    }

    IEnumerator IEnumerable.GetEnumerator() => GetEnumerator();
}
```

### 💡 **Recognition Clues**

* `IEnumerable` / `IEnumerator` interfaces.
* Use of `yield return`.
* Custom iteration logic over internal data.

---

## **5. Mediator Pattern**

> Defines an object that encapsulates how a set of objects interact.

### 🔍 **How to Recognize It**

* A central **Mediator class** handles communication.
* Colleague classes **do not reference each other directly**, only the mediator.
* Used in **UI systems**, **chatrooms**, or **event hubs**.

### ✅ **Typical C# Example**

```csharp
public interface IMediator
{
    void Notify(object sender, string ev);
}

public class ConcreteMediator : IMediator
{
    public Button Button { get; set; }
    public TextBox TextBox { get; set; }

    public void Notify(object sender, string ev)
    {
        if (ev == "Click") TextBox.Clear();
    }
}

public class Button
{
    private readonly IMediator _mediator;
    public Button(IMediator mediator) => _mediator = mediator;
    public void Click() => _mediator.Notify(this, "Click");
}

public class TextBox
{
    private readonly IMediator _mediator;
    public TextBox(IMediator mediator) => _mediator = mediator;
    public void Clear() => Console.WriteLine("TextBox cleared.");
}
```

### 💡 **Recognition Clues**

* A central coordinator class (Mediator).
* Other objects call `mediator.Notify(this, eventName)` instead of each other.
* Common in **UI event systems**, **message brokers**, or **CQRS event buses**.

---

## **6. Memento Pattern**

> Captures an object’s internal state so it can be restored later.

### 🔍 **How to Recognize It**

* A **Memento** class that stores state.
* An **Originator** that creates and restores the memento.
* A **Caretaker** that stores the memento history.

### ✅ **Typical C# Example**

```csharp
public class EditorMemento
{
    public string Content { get; }
    public EditorMemento(string content) => Content = content;
}

public class Editor
{
    public string Content { get; private set; } = "";
    public void Type(string text) => Content += text;
    public EditorMemento Save() => new EditorMemento(Content);
    public void Restore(EditorMemento m) => Content = m.Content;
}
```

### 💡 **Recognition Clues**

* Methods like `Save()` and `Restore()`.
* Separate class storing snapshots of state.
* Often used for **undo/redo**, **checkpointing**, or **state recovery**.

---

## **7. Observer Pattern**

> Establishes a one-to-many dependency so when one object changes, others are notified.

### 🔍 **How to Recognize It**

* An **ISubject** interface with `RegisterObserver`, `RemoveObserver`, and `NotifyObservers`.
* Observers implement an `Update()` method.
* Subject holds a **collection of observers**.

### ✅ **Typical C# Example**

```csharp
public interface IObserver { void Update(string message); }
public interface ISubject
{
    void RegisterObserver(IObserver o);
    void NotifyObservers(string msg);
}

public class WeatherStation : ISubject
{
    private readonly List<IObserver> _observers = new List<IObserver>();
    public void RegisterObserver(IObserver o) => _observers.Add(o);
    public void NotifyObservers(string msg)
    {
        foreach (var o in _observers) o.Update(msg);
    }
}
```

### 💡 **Recognition Clues**

* One-to-many relationship.
* Observer list + `NotifyObservers()` method.
* Common in **event-driven systems**, **UI bindings**, or **backend notifications**.

---

## **8. State Pattern**

> Allows an object to change its behavior when its internal state changes.

### 🔍 **How to Recognize It**

* A **context** class delegates behavior to a **state interface**.
* Multiple concrete state classes implement the same interface.
* The context holds a **reference to the current state**.

### ✅ **Typical C# Example**

```csharp
public interface IState { void Handle(Context context); }

public class Context
{
    public IState State { get; set; }
    public Context(IState state) => State = state;
    public void Request() => State.Handle(this);
}

public class OpenState : IState
{
    public void Handle(Context context)
    {
        Console.WriteLine("Already open.");
        context.State = new ClosedState();
    }
}

public class ClosedState : IState
{
    public void Handle(Context context)
    {
        Console.WriteLine("Opening file...");
        context.State = new OpenState();
    }
}
```

### 💡 **Recognition Clues**

* `Context` delegates to `State` object.
* Multiple classes implement a shared interface.
* Look for transitions like `context.State = new OtherState()`.

---

## **9. Strategy Pattern**

> Defines a family of algorithms and makes them interchangeable.

### 🔍 **How to Recognize It**

* A **Strategy interface** with multiple **implementations**.
* A **Context class** uses a strategy via composition.
* Behavior can be **swapped dynamically**.

### ✅ **Typical C# Example**

```csharp
public interface ICompressionStrategy { void Compress(string file); }

public class ZipCompression : ICompressionStrategy
{
    public void Compress(string file) => Console.WriteLine("Zipping " + file);
}

public class GzipCompression : ICompressionStrategy
{
    public void Compress(string file) => Console.WriteLine("Gzipping " + file);
}

public class Compressor
{
    private ICompressionStrategy _strategy;
    public Compressor(ICompressionStrategy strategy) => _strategy = strategy;
    public void SetStrategy(ICompressionStrategy strategy) => _strategy = strategy;
    public void CompressFile(string file) => _strategy.Compress(file);
}
```

### 💡 **Recognition Clues**

* Interface for interchangeable algorithms.
* Context class delegates work to strategy.
* Often used in **payment processing**, **sorting**, **caching**, or **compression**.

---

## **10. Template Method Pattern**

> Defines the skeleton of an algorithm, letting subclasses redefine specific steps.

### 🔍 **How to Recognize It**

* An **abstract base class** with a **final (non-virtual)** method that calls **abstract or virtual** methods.
* Subclasses override specific steps.
* Common in frameworks, importers, or report generators.

### ✅ **Typical C# Example**

```csharp
public abstract class DataImporter
{
    public void Import()
    {
        ReadData();
        ProcessData();
        SaveData();
    }

    protected abstract void ReadData();
    protected abstract void ProcessData();
    protected virtual void SaveData() => Console.WriteLine("Saving to default storage...");
}

public class CsvImporter : DataImporter
{
    protected override void ReadData() => Console.WriteLine("Reading CSV...");
    protected override void ProcessData() => Console.WriteLine("Processing CSV...");
}
```

### 💡 **Recognition Clues**

* Base class defines a **final “template” method** (e.g., `Import()`).
* Steps are defined in **abstract/virtual methods**.
* Subclasses customize behavior.

---

## **11. Visitor Pattern**

> Separates algorithms from the objects on which they operate.

### 🔍 **How to Recognize It**

* Visitor interface with **`Visit()` methods** for different types.
* Elements implement an **`Accept(Visitor)`** method.
* Common when new operations are added frequently.

### ✅ **Typical C# Example**

```csharp
public interface IVisitor
{
    void VisitCircle(Circle circle);
    void VisitRectangle(Rectangle rectangle);
}

public interface IShape
{
    void Accept(IVisitor visitor);
}

public class Circle : IShape
{
    public void Accept(IVisitor visitor) => visitor.VisitCircle(this);
}

public class Rectangle : IShape
{
    public void Accept(IVisitor visitor) => visitor.VisitRectangle(this);
}
```

### 💡 **Recognition Clues**

* Double dispatch (`element.Accept(visitor)` calls `visitor.Visit(element)`).
* `Visit` methods are **overloaded for different types**.
* Common in **serialization**, **UI rendering**, **compilers**, and **AST processing**.

---

# 🧾 **Quick Recognition Summary**

| Pattern                     | Intent                                   | Recognition Clues in C#                  |
| --------------------------- | ---------------------------------------- | ---------------------------------------- |
| **Chain of Responsibility** | Pass request along a handler chain       | `_next?.Handle()` pattern                |
| **Command**                 | Encapsulate actions as objects           | Classes with `Execute()`                 |
| **Interpreter**             | Represent grammar or rules               | Classes with `Interpret()`               |
| **Iterator**                | Sequential access to collection          | Implements `IEnumerable` / `IEnumerator` |
| **Mediator**                | Centralize communication                 | Calls to `mediator.Notify()`             |
| **Memento**                 | Save/restore state                       | `Save()` and `Restore()` methods         |
| **Observer**                | Notify dependents automatically          | `NotifyObservers()` / `Update()`         |
| **State**                   | Change behavior dynamically              | `context.State = new OtherState()`       |
| **Strategy**                | Swap algorithms at runtime               | `_strategy.Execute()` / `SetStrategy()`  |
| **Template Method**         | Skeleton of an algorithm                 | Base class with `abstract` steps         |
| **Visitor**                 | Separate operations from data structures | `Accept(visitor)` + `Visit(element)`     |

---

# 🕵️‍♂️ **How to Detect Behavioral Patterns in Existing Code**

| Clue                                           | Likely Pattern          |
| ---------------------------------------------- | ----------------------- |
| Repeated `Execute()` calls                     | Command                 |
| Classes named `Handler` forming a chain        | Chain of Responsibility |
| Event-like subscriptions                       | Observer / Mediator     |
| Conditional behavior replaced by state classes | State                   |
| Interfaces ending in “Strategy”                | Strategy                |
| Base class method calling abstract ones        | Template Method         |
| Visitor pattern (double dispatch)              | Visitor                 |
| Use of mementos or checkpoints                 | Memento                 |

---

# ✅ **Summary**

Behavioral patterns describe **object collaboration** — who talks to whom, and how.
Recognizing them helps you:

* Predict system flow,
* Add new behaviors safely,
* Refactor large codebases into maintainable architectures.

| Category                     | Focus                       | Example Usage             |
| ---------------------------- | --------------------------- | ------------------------- |
| **Communication Management** | Mediator, Observer, Chain   | Event systems, middleware |
| **Behavior Encapsulation**   | Strategy, Command, Template | Reusable algorithms       |
| **State & Logic Management** | State, Memento, Interpreter | Workflow engines          |
| **Traversal & Extension**    | Iterator, Visitor           | Collections, AST, APIs    |

> 🧩 **Pro tip:**
> When you see **behavior encapsulated in objects** (not just methods), you’re looking at a **behavioral pattern**.
