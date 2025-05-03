# System design guide

## High Level Design

### Step 1: Fundamentals

- Serveless vs Serverful
- Horizontal vs Vertical
- What are threads?
- What are pages?
- How does the internet works?

### Step 2: Databases

- SQL vs NoSQL DBs
- In-memory DBs
- Data Replication & Migration
- Data Partiotioning
- Sharding

### Step 3: Consistency vs Availability

- Data Consistency & Its levels
- Isolation & Its levels
- CAP theorem

### Step 4: Cache

- What is cache? (Redis, Memcached)
- Write Policies: write back, through & around
- Replacement Policies: LFU, LRU, Segmented LRU etc.
- Content Delivery Networks (CDNs)

### Step 5: Networking

- TCP vs UDP
- What is htpp (1/2/3) & https
- Web sockets
- WebRTC & video streaming

### Step 6: Load Balancers

- Load balancing algorithms (Stateless & stateful)
- Consistent Hashing
- Proxy & Reverse Proxy
- Rate limiting

### Step 7: Message queues

- Assynchronous Processing (Kafka, RabbitMQ)
- Publisher-Subscriber Model

### Step 8: Monoliths vs Microservices

- Why microservices?
- Concept of Single Point of Failure
- Avoiding Cascading Failures
- Containerization (Docker)
- Migrating to microservices

### Step 9: Monitoring and Logging

- Logging events & monitoring metrics
- Anomaly Detection

### Step 10: Security

- Tokens for auth
- SSO & OAuth
- Acess Control Lists & Rule Engines
- Encryption

### Step 11: System design tradeoffs

- Push vs Pull Architecture
- Consistency vs Availability
- SQL vs NoSQL DBs
- Memory vs Latency
- Throughput vs Latency
- Accuracy vs Latency

### Step 12: Practice every fucking step

Try to build:

- Youtube
- Twitter
- Whatsapp
- Uber
- Amazon
- Dropbox/Google drive
- Netflix
- Instagram
- Zoom
- Booking.com/Airbnb
