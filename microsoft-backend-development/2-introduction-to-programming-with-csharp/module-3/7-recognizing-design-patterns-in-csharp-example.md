# **Example: Recognizing Design Patterns in C# Code (Improved Version)**

## **Introduction**

Recognizing design patterns in code is an important skill in software architecture and maintenance. It allows developers to understand *why* a piece of code was written a certain way and *how* to extend or refactor it without breaking its intended behavior.

This example demonstrates how to identify and explain multiple design patterns in a single C# program. The analyzed code implements a **notification system** using two major design patterns: **Factory Method** and **Observer**.

---

## **C# Code Example**

```csharp
using System;
using System.Collections.Generic;

// =============== INTERFACES ===============

public interface INotification
{
    void Send(string message);
}

public interface IObserver
{
    void Update(string message);
}

public interface ISubject
{
    void RegisterObserver(IObserver observer);
    void RemoveObserver(IObserver observer);
    void NotifyObservers(string message);
}

// =============== NOTIFICATION IMPLEMENTATIONS ===============

public class EmailNotification : INotification
{
    public void Send(string message)
    {
        Console.WriteLine("Printing e-mail message: " + message);
    }
}

public class SMSNotification : INotification
{
    public void Send(string message)
    {
        Console.WriteLine("Printing SMS message: " + message);
    }
}

public class PushNotification : INotification
{
    public void Send(string message)
    {
        Console.WriteLine("Printing push notification: " + message);
    }
}

// =============== FACTORY METHOD PATTERN ===============

public class NotificationFactory
{
    private readonly Dictionary<string, Func<INotification>> _registry;

    public NotificationFactory()
    {
        _registry = new Dictionary<string, Func<INotification>>();
        _registry.Add("Email", () => new EmailNotification());
        _registry.Add("SMS", () => new SMSNotification());
        _registry.Add("Push", () => new PushNotification());
    }

    public INotification CreateNotification(string channel)
    {
        Func<INotification> creator;
        if (_registry.TryGetValue(channel, out creator))
        {
            return creator();
        }
        else
        {
            throw new ArgumentException("Invalid notification channel: " + channel);
        }
    }
}

// =============== OBSERVER PATTERN ===============

public class NotificationService : ISubject
{
    private readonly List<IObserver> _observers = new List<IObserver>();
    private readonly NotificationFactory _factory = new NotificationFactory();

    public void RegisterObserver(IObserver observer)
    {
        _observers.Add(observer);
    }

    public void RemoveObserver(IObserver observer)
    {
        _observers.Remove(observer);
    }

    public void NotifyObservers(string message)
    {
        foreach (var observer in _observers)
        {
            observer.Update(message);
        }
    }

    public void SendNotification(string channel, string message)
    {
        INotification notification = _factory.CreateNotification(channel);
        notification.Send(message);
        NotifyObservers(message);
    }
}

// =============== OBSERVERS IMPLEMENTATIONS ===============

public class PhoneDisplay : IObserver
{
    public void Update(string message)
    {
        Console.WriteLine("Phone display received notification: " + message);
    }
}

public class DesktopDisplay : IObserver
{
    public void Update(string message)
    {
        Console.WriteLine("Desktop display received notification: " + message);
    }
}

// =============== EXECUTION ===============

class Program
{
    static void Main()
    {
        NotificationService notificationService = new NotificationService();
        PhoneDisplay phoneDisplay = new PhoneDisplay();
        DesktopDisplay desktopDisplay = new DesktopDisplay();

        notificationService.RegisterObserver(phoneDisplay);
        notificationService.RegisterObserver(desktopDisplay);

        notificationService.SendNotification("Email", "Hello, this is an email notification!");
        notificationService.SendNotification("SMS", "Hello, this is an SMS notification!");
        notificationService.SendNotification("Push", "Hello, this is a push notification!");
    }
}
```

---

## **Recognized Design Patterns**

### 🎯 **1. Factory Method Pattern**

#### **Where it appears:**

```csharp
public class NotificationFactory
{
    private readonly Dictionary<string, Func<INotification>> _registry;

    public NotificationFactory()
    {
        _registry = new Dictionary<string, Func<INotification>>();
        _registry.Add("Email", () => new EmailNotification());
        _registry.Add("SMS", () => new SMSNotification());
        _registry.Add("Push", () => new PushNotification());
    }

    public INotification CreateNotification(string channel)
    {
        Func<INotification> creator;
        if (_registry.TryGetValue(channel, out creator))
        {
            return creator();
        }
        else
        {
            throw new ArgumentException("Invalid notification channel: " + channel);
        }
    }
}
```

#### **Why it’s the Factory Method Pattern:**

* The **object creation logic** is centralized in a separate class.
* The client (`NotificationService`) **does not know** which concrete class will be instantiated.
* This pattern provides **flexibility** — new notification types (like `PushNotification`) can be added by simply extending the factory’s registry.

#### **Pattern category:** Creational

#### **Main benefit:** Decouples **object creation** from **object usage**.

---

### 🔔 **2. Observer Pattern**

#### **Where it appears:**

```csharp
public class NotificationService : ISubject
{
    private readonly List<IObserver> _observers = new List<IObserver>();

    public void RegisterObserver(IObserver observer) => _observers.Add(observer);
    public void RemoveObserver(IObserver observer) => _observers.Remove(observer);
    public void NotifyObservers(string message)
    {
        foreach (var observer in _observers)
            observer.Update(message);
    }
}
```

#### **Why it’s the Observer Pattern:**

* The **subject** (`NotificationService`) maintains a list of **observers** (`PhoneDisplay`, `DesktopDisplay`).
* When a notification is sent, the subject **notifies all observers** automatically.
* Observers are **loosely coupled** — they can be added or removed dynamically.

#### **Pattern category:** Behavioral

#### **Main benefit:** Enables **event-driven updates** across multiple components without direct dependencies.

---

## **3. How the Patterns Collaborate**

| Role                             | Design Pattern   | Responsibility                                    |
| -------------------------------- | ---------------- | ------------------------------------------------- |
| `NotificationFactory`            | Factory Method   | Creates the appropriate `INotification` instance. |
| `NotificationService`            | Observer Subject | Manages and notifies all observers.               |
| `PhoneDisplay`, `DesktopDisplay` | Observers        | React to events published by the service.         |

### 🔁 **Flow Overview:**

1. The user sends a notification request.
2. `NotificationService` delegates object creation to the **Factory**.
3. The **Observer Pattern** updates all registered subscribers once a message is sent.

---

## **4. Benefits of This Design**

This code embodies multiple **SOLID principles**:

* **Single Responsibility:** Each class has one clear purpose.
* **Open/Closed Principle:** You can add new notification channels or observers without changing existing logic.
* **Dependency Inversion:** High-level modules depend on abstractions (`INotification`, `IObserver`), not concrete classes.

Together, these patterns make the system:

* **Extensible:** New behaviors can be added easily.
* **Testable:** Mocking interfaces simplifies unit testing.
* **Maintainable:** The codebase is logically modular and predictable.

---

## **5. Summary**

| Pattern            | Category   | Function in Code                                             | Key Advantage                                          |
| ------------------ | ---------- | ------------------------------------------------------------ | ------------------------------------------------------ |
| **Factory Method** | Creational | Creates proper notification objects (`Email`, `SMS`, `Push`) | Decouples object creation from logic                   |
| **Observer**       | Behavioral | Manages dynamic event updates across displays                | Promotes loose coupling and event-driven communication |

> ✅ **Conclusion:** This program implements a *hybrid pattern design* — the Factory Method pattern for object creation and the Observer pattern for event-driven updates. The combination exemplifies how multiple patterns can work together to create scalable, maintainable backend architectures.
