# 📝 Problem Decomposition & UML Documentation

This document contains **problem decomposition** (top-down, breakdown, modularization) for three projects at different difficulty levels, along with **UML diagrams** (Class, Sequence, Activity, Deployment) and **actor-action tables**. A final section shows **module dependencies** for all projects.

---

## 🟢 Beginner Level – Digital Alarm Clock

### Problem Decomposition

**Main Goal**: Build a digital alarm clock that displays time and rings an alarm at a set time.

**Top-Down Approach**:

* Display current time.
* Allow users to set an alarm.
* Trigger a notification when the alarm time is reached.

**Breakdown into Smaller Components**:

* **Time Management**: Track and display real-time clock updates.
* **Alarm Feature**: Set and check alarm time.
* **Notification**: Alert user with sound or visual message.

**Modularization**:

* `Time Module` – Handles current time display.
* `Alarm Module` – Stores alarm settings, triggers when matched.
* `Notification Module` – Produces alarm sound/alert.

### Actors and Actions

| Actor | Action     |
| ----- | ---------- |
| User  | Set Alarm  |
| User  | View Time  |
| User  | Stop Alarm |

### UML Diagrams

#### Class Diagram

```mermaid
classDiagram
class Alarm {
  +time: string
  +isActive: bool
  +setTime(time)
  +activate()
  +deactivate()
}

class Time {
  +currentTime: string
  +updateTime()
  +getCurrentTime()
}

class Notification {
  +message: string
  +playSound()
  +showNotification()
}

Alarm --> Time
Alarm --> Notification
```

#### Sequence Diagram

```mermaid
sequenceDiagram
actor User
participant AlarmClock
participant Alarm
participant Notification

User ->> AlarmClock: Set Alarm
AlarmClock ->> Alarm: Save Alarm Time
Alarm ->> Time: Compare with Current Time
Time -->> Alarm: Matches
Alarm ->> Notification: Trigger Alarm
Notification -->> User: Play Sound + Display
```

---

## 🟡 Intermediate Level – Library Book Management System

### Problem Decomposition

**Main Goal**: Manage books in a library, including borrowing and returning by users.

**Top-Down Approach**:

* Add/remove/search books.
* Borrow/return functionality.
* Track user transactions.

**Breakdown into Smaller Components**:

* **Book Management**: Add/remove books, search catalog.
* **User Transactions**: Record borrowing/returning.
* **Catalog Search**: Filter/search books by title, author, ID.

**Modularization**:

* `Book Module` – Stores details of each book.
* `User Module` – Handles member/librarian roles.
* `Transaction Module` – Records borrow/return history.
* `Library Catalog` – Provides search and availability functions.

### Actors and Actions

| Actor     | Action      |
| --------- | ----------- |
| Member    | Borrow Book |
| Member    | Return Book |
| Member    | Search Book |
| Librarian | Add Book    |
| Librarian | Remove Book |

### UML Diagrams

#### Class Diagram

```mermaid
classDiagram
class Book {
  +id: int
  +title: string
  +author: string
  +isAvailable: bool
  +borrow()
  +returnBook()
}

class User {
  +id: int
  +name: string
  +role: string
}

class Transaction {
  +transactionId: int
  +borrowDate: date
  +returnDate: date
}

class LibraryCatalog {
  +books: List~Book~
  +search(title)
}

User --> Transaction
Transaction --> Book
LibraryCatalog --> Book
```

#### Activity Diagram (Borrow Book)

```mermaid
flowchart TD
A[Start] --> B[Search Book]
B -->|Book Available| C[Request Book]
B -->|Book Not Available| D[Show Unavailable]
C --> E[Update Book Status]
E --> F[Create Transaction Record]
F --> G[Confirm Borrow]
D --> H[End]
G --> H[End]
```

#### Sequence Diagram

```mermaid
sequenceDiagram
actor Member
participant LibrarySystem
participant Catalog
participant Book
participant Transaction

Member ->> LibrarySystem: Request to Borrow Book
LibrarySystem ->> Catalog: Search Book
Catalog -->> LibrarySystem: Book Found
LibrarySystem ->> Book: Check Availability
Book -->> LibrarySystem: Available
LibrarySystem ->> Transaction: Create Record
Transaction -->> Member: Borrow Confirmed
```

---

## 🔴 Advanced Level – Real-Time Chat Application

### Problem Decomposition

**Main Goal**: Enable multiple users to chat in real time.

**Top-Down Approach**:

* User authentication.
* Send/receive messages.
* Manage chat rooms.
* Store chat history.

**Breakdown into Smaller Components**:

* **User Authentication**: Login/logout sessions.
* **Messaging**: Send/receive, broadcast messages.
* **Chat Rooms**: Manage users and messages in groups.
* **Database**: Store chat history, retrieve past messages.

**Modularization**:

* `User Module` – Authentication and sessions.
* `Message Module` – Sending and receiving.
* `ChatRoom Module` – Group messaging logic.
* `Database Handler` – Save/load chat history.
* `Session Manager` – Manage live sessions.

### Actors and Actions

| Actor | Action            |
| ----- | ----------------- |
| User  | Login             |
| User  | Send Message      |
| User  | Join Chat Room    |
| User  | View Chat History |
| Admin | Manage Users      |
| Admin | Moderate Chats    |

### UML Diagrams

#### Class Diagram

```mermaid
classDiagram
class User {
  +id: int
  +username: string
  +password: string
  +login()
  +logout()
}

class Message {
  +id: int
  +content: string
  +timestamp: datetime
  +send()
}

class ChatRoom {
  +id: int
  +name: string
  +users: List~User~
  +messages: List~Message~
  +addUser(user)
  +removeUser(user)
}

class SessionManager {
  +createSession(user)
  +validateSession(token)
  +endSession(user)
}

class DatabaseHandler {
  +saveMessage(message)
  +loadChatHistory(roomId)
}

User --> SessionManager
User --> ChatRoom
ChatRoom --> Message
DatabaseHandler --> Message
```

#### Sequence Diagram (Send Message)

```mermaid
sequenceDiagram
actor User
participant ClientApp
participant Server
participant ChatRoom
participant Database

User ->> ClientApp: Type Message
ClientApp ->> Server: Send Message via WebSocket
Server ->> ChatRoom: Deliver Message
ChatRoom ->> Database: Store Message
ChatRoom -->> ClientApp: Broadcast to All Users
```

#### Deployment Diagram

```mermaid
graph TD
A[User Device] -->|WebSocket/HTTP| B[Web Server]
B --> C[Auth Service]
B --> D[Messaging Service]
D --> E[Database]
D --> F[Real-time Notification Service]
```

---

## 🏗 Module Dependencies – All Projects

```mermaid
graph TD
    %% Beginner: Digital Alarm Clock
    subgraph DigitalAlarmClock
        TimeModule[Time Module]
        AlarmModule[Alarm Module]
        NotificationModule[Notification Module]

        TimeModule --> AlarmModule
        AlarmModule --> NotificationModule
    end

    %% Intermediate: Library Book Management System
    subgraph LibrarySystem
        BookModule[Book Module]
        UserModule[User Module]
        TransactionModule[Transaction Module]
        CatalogModule[Library Catalog Module]

        UserModule --> TransactionModule
        TransactionModule --> BookModule
        CatalogModule --> BookModule
    end

    %% Advanced: Real-Time Chat Application
    subgraph ChatApp
        AuthModule[User/Auth Module]
        MessageModule[Message Module]
        ChatRoomModule[ChatRoom Module]
        DatabaseModule[Database Handler Module]
        SessionModule[Session Manager Module]

        AuthModule --> SessionModule
        AuthModule --> ChatRoomModule
        MessageModule --> ChatRoomModule
        MessageModule --> DatabaseModule
        ChatRoomModule --> DatabaseModule
    end
```

### ✅ Explanation

* **Digital Alarm Clock (Beginner)**

  * `Time Module` feeds `Alarm Module` which triggers the `Notification Module`.

* **Library Book Management System (Intermediate)**

  * `User Module` interacts with `Transaction Module`.
  * `Transaction Module` updates `Book Module`.
  * `Library Catalog Module` queries `Book Module` for searches.

* **Real-Time Chat Application (Advanced)**

  * `Auth Module` manages login and session info via `Session Module`.
  * `Message Module` handles sending messages to `ChatRoom Module` and persists them in `Database Module`.
  * `ChatRoom Module` coordinates message distribution and storage.

  
