# 🧩 **Recognizing Structural Design Patterns in C#**

## **1. Adapter Pattern**

> Allows incompatible interfaces to work together by translating one interface into another.

### 🔍 **How to Recognize It**

Look for:

* A class that **wraps another class** to make it compatible with a different interface.
* A **target interface** that defines the expected behavior.
* A **wrapper class (adapter)** that implements the target interface but **delegates calls** to an incompatible class.

### ✅ **Typical C# Example**

```csharp
// Target interface expected by the system
public interface IMessageSender
{
    void Send(string message);
}

// Existing (incompatible) class
public class LegacyEmailService
{
    public void SendMail(string subject, string body)
    {
        Console.WriteLine("Legacy email sent: " + subject + " - " + body);
    }
}

// Adapter class
public class EmailAdapter : IMessageSender
{
    private readonly LegacyEmailService _legacyService;

    public EmailAdapter(LegacyEmailService legacyService)
    {
        _legacyService = legacyService;
    }

    public void Send(string message)
    {
        _legacyService.SendMail("AdapterSubject", message);
    }
}
```

### 💡 **Recognition Clues**

* A class implements an interface but internally calls a **different class’s method** with **different signatures**.
* Common naming pattern: *Adapter*, *Wrapper*, or *Bridge*.
* Often seen when integrating **third-party APIs** or **legacy systems**.

---

## **2. Bridge Pattern**

> Decouples an abstraction from its implementation so that both can vary independently.

### 🔍 **How to Recognize It**

Look for:

* An **abstraction** class that holds a reference to an **implementation interface**.
* Two hierarchies evolving separately (e.g., `Shape` vs `Renderer`).
* Implementation can be swapped dynamically.

### ✅ **Typical C# Example**

```csharp
// Implementation hierarchy
public interface IRenderer
{
    void Render(string shape);
}

public class VectorRenderer : IRenderer
{
    public void Render(string shape) => Console.WriteLine("Drawing " + shape + " as vectors.");
}

public class RasterRenderer : IRenderer
{
    public void Render(string shape) => Console.WriteLine("Drawing " + shape + " as pixels.");
}

// Abstraction hierarchy
public abstract class Shape
{
    protected IRenderer _renderer;
    protected Shape(IRenderer renderer) => _renderer = renderer;

    public abstract void Draw();
}

public class Circle : Shape
{
    public Circle(IRenderer renderer) : base(renderer) { }
    public override void Draw() => _renderer.Render("Circle");
}
```

### 💡 **Recognition Clues**

* Abstraction and implementation hierarchies exist in parallel.
* One class **“bridges”** between **high-level logic** and **low-level details**.
* Often found in rendering engines, data access abstractions, or messaging layers.

---

## **3. Composite Pattern**

> Composes objects into tree structures to represent part-whole hierarchies.

### 🔍 **How to Recognize It**

Look for:

* A **common interface or base class** shared by both “leaf” and “composite” nodes.
* Composite objects contain **collections of the same interface type**.
* Recursive calls — composites delegate operations to child components.

### ✅ **Typical C# Example**

```csharp
public interface IFileSystemItem
{
    void Display(int depth = 0);
}

public class File : IFileSystemItem
{
    private readonly string _name;
    public File(string name) { _name = name; }
    public void Display(int depth = 0) => Console.WriteLine(new string('-', depth) + _name);
}

public class Directory : IFileSystemItem
{
    private readonly string _name;
    private readonly List<IFileSystemItem> _children = new List<IFileSystemItem>();

    public Directory(string name) { _name = name; }

    public void Add(IFileSystemItem item) => _children.Add(item);

    public void Display(int depth = 0)
    {
        Console.WriteLine(new string('-', depth) + _name);
        foreach (var child in _children)
            child.Display(depth + 2);
    }
}
```

### 💡 **Recognition Clues**

* Same interface used for both individual and container objects.
* Recursive `foreach` over child elements of the same type.
* Methods like `Add`, `Remove`, `Display` hint at composition.

---

## **4. Decorator Pattern**

> Dynamically adds responsibilities to an object without modifying its structure.

### 🔍 **How to Recognize It**

Look for:

* A class that **implements the same interface** as another class.
* It **wraps another instance** of that same interface.
* Calls to the wrapped instance with **added behavior** before or after.

### ✅ **Typical C# Example**

```csharp
public interface INotifier
{
    void Send(string message);
}

public class EmailNotifier : INotifier
{
    public void Send(string message) => Console.WriteLine("Sending Email: " + message);
}

public class SMSDecorator : INotifier
{
    private readonly INotifier _notifier;
    public SMSDecorator(INotifier notifier) { _notifier = notifier; }

    public void Send(string message)
    {
        _notifier.Send(message);
        Console.WriteLine("Also sending SMS: " + message);
    }
}
```

### 💡 **Recognition Clues**

* Class implements same interface as the object it wraps.
* Constructor accepts another object of the same interface.
* Adds functionality without changing the original object’s class.

---

## **5. Facade Pattern**

> Provides a unified interface to a set of interfaces in a subsystem, simplifying complex interactions.

### 🔍 **How to Recognize It**

Look for:

* A single “entry point” class that delegates to **multiple subsystems**.
* The subsystem classes are hidden from the client.
* The facade exposes **high-level, easy-to-use methods**.

### ✅ **Typical C# Example**

```csharp
public class VideoEncoder
{
    public void Encode(string video) => Console.WriteLine("Encoding video: " + video);
}

public class VideoCompressor
{
    public void Compress(string video) => Console.WriteLine("Compressing video: " + video);
}

public class VideoUploader
{
    public void Upload(string video) => Console.WriteLine("Uploading video: " + video);
}

public class VideoFacade
{
    private readonly VideoEncoder _encoder = new VideoEncoder();
    private readonly VideoCompressor _compressor = new VideoCompressor();
    private readonly VideoUploader _uploader = new VideoUploader();

    public void ProcessVideo(string video)
    {
        _encoder.Encode(video);
        _compressor.Compress(video);
        _uploader.Upload(video);
    }
}
```

### 💡 **Recognition Clues**

* A “service” or “manager” class that combines multiple operations.
* Simplified, single-method interface for complex systems.
* Often named `Facade`, `Manager`, or `Service`.

---

## **6. Flyweight Pattern**

> Reduces memory usage by sharing common state among multiple objects.

### 🔍 **How to Recognize It**

Look for:

* A **factory or cache** that returns shared objects.
* Objects with **intrinsic state** (shared) and **extrinsic state** (unique per use).
* Heavy use of **object reuse** and **dictionary-based storage**.

### ✅ **Typical C# Example**

```csharp
public class Character
{
    private readonly char _symbol;
    public Character(char symbol) { _symbol = symbol; }

    public void Display(int size)
    {
        Console.WriteLine($"Character: {_symbol} Size: {size}");
    }
}

public class CharacterFactory
{
    private readonly Dictionary<char, Character> _cache = new Dictionary<char, Character>();

    public Character GetCharacter(char symbol)
    {
        if (!_cache.ContainsKey(symbol))
            _cache[symbol] = new Character(symbol);
        return _cache[symbol];
    }
}
```

### 💡 **Recognition Clues**

* Factory caching identical instances.
* Shared objects with immutable internal state.
* `Dictionary`, `Cache`, or `Pool` used for object reuse.

---

## **7. Proxy Pattern**

> Provides a surrogate or placeholder for another object to control access to it.

### 🔍 **How to Recognize It**

Look for:

* A class that **implements the same interface** as another.
* The proxy forwards requests but may **add behavior** like access control, caching, or logging.
* Used when direct access to the real object is **expensive or restricted**.

### ✅ **Typical C# Example**

```csharp
public interface IImage
{
    void Display();
}

public class RealImage : IImage
{
    private readonly string _filename;
    public RealImage(string filename)
    {
        _filename = filename;
        Console.WriteLine("Loading " + filename);
    }

    public void Display() => Console.WriteLine("Displaying " + _filename);
}

public class ImageProxy : IImage
{
    private RealImage _realImage;
    private readonly string _filename;

    public ImageProxy(string filename)
    {
        _filename = filename;
    }

    public void Display()
    {
        if (_realImage == null)
            _realImage = new RealImage(_filename);
        _realImage.Display();
    }
}
```

### 💡 **Recognition Clues**

* Proxy and real object share the same interface.
* Proxy controls or delays access to the real object.
* Often used for **lazy loading**, **authorization**, or **remote access**.

---

# 🧠 **Quick Recognition Summary**

| Pattern       | Core Intent                              | C# Recognition Clues                                                        | Common Use Case                        |
| ------------- | ---------------------------------------- | --------------------------------------------------------------------------- | -------------------------------------- |
| **Adapter**   | Convert one interface to another         | Class implements interface but delegates to incompatible class              | Integrating legacy or external systems |
| **Bridge**    | Separate abstraction from implementation | Two hierarchies (abstraction + implementation)                              | UI rendering, data drivers             |
| **Composite** | Compose objects in tree structures       | Recursive interface, `Add/Remove`, shared interface for both leaf/composite | File systems, menu hierarchies         |
| **Decorator** | Add behavior dynamically                 | Class wraps same interface, calls inner object                              | Logging, caching, security layers      |
| **Facade**    | Simplify subsystem usage                 | One class delegates to many others                                          | Service layers, API gateways           |
| **Flyweight** | Share common state                       | Factory returns cached/shared objects                                       | Game engines, text rendering           |
| **Proxy**     | Control or defer access                  | Same interface, lazy initialization or access control                       | Remote calls, caching, auth proxies    |

---

# 🕵️‍♂️ **General Recognition Strategy**

When reading C# code:

1. **Find Wrappers.**
   If one class holds another instance of a similar or related interface → it’s likely a *Decorator*, *Adapter*, or *Proxy*.
2. **Check Intent.**

   * Is it adapting? → *Adapter*
   * Is it restricting access? → *Proxy*
   * Is it extending behavior? → *Decorator*
3. **Look for Hierarchies.**
   Two hierarchies that can vary independently? → *Bridge*.
4. **Recursive Structures.**
   When classes contain collections of themselves → *Composite*.
5. **Unified Entry Points.**
   When a class simplifies many others → *Facade*.
6. **Caches or Object Pools.**
   When identical objects are reused → *Flyweight*.

---

# ✅ **Summary Table**

| Category   | Pattern       | Focus                                        | Typical Keyword / Clue in C#               |
| ---------- | ------------- | -------------------------------------------- | ------------------------------------------ |
| Structural | **Adapter**   | Interface compatibility                      | “Adapter”, “Wrapper”, interface conversion |
| Structural | **Bridge**    | Separation of abstraction and implementation | Two hierarchies connected via composition  |
| Structural | **Composite** | Hierarchical trees                           | `Add()`, recursion, shared interface       |
| Structural | **Decorator** | Behavior extension                           | Wraps same interface                       |
| Structural | **Facade**    | Simplified subsystem access                  | “Service”, “Manager”, “Facade”             |
| Structural | **Flyweight** | Memory optimization                          | Object pool, `Dictionary`, caching         |
| Structural | **Proxy**     | Access control or lazy load                  | Same interface, deferred creation          |
