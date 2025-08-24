# 🩺 Problem 2: Online Health Monitoring System (Bottom-Up Approach)

**Problem Statement**:
Decompose the creation of an online health monitoring system that tracks **physical activity**, **sleep**, and **heart rate**. Decide which approach (top-down or bottom-up) is more suitable and explain why.

---

## ✅ Step 1: Identify the Main Goal

The main goal is to build a system that helps users monitor their health by tracking:

* Physical activity
* Sleep patterns
* Heart rate

But instead of starting broad (like in **top-down**), we start **small** and focus on individual features first.

---

## ✅ Step 2: Choose the Bottom-Up Approach

We choose **bottom-up** because:

* We can build **independent features** first (activity tracker, sleep tracker, heart rate monitor).
* Each feature can be **developed and tested separately**.
* Later, we combine them into a **full system**.
  This is useful when features are **well-known** but the overall system integration can be figured out gradually.

---

## ✅ Step 3: Break Down into Small Features & Tasks

### 1. Physical Activity Tracker

* Step counter module.
* Calories burned calculator.
* Activity logging (running, cycling, walking).

### 2. Sleep Monitoring

* Track hours slept.
* Detect sleep cycles (light/deep sleep).
* Generate daily/weekly sleep reports.

### 3. Heart Rate Monitoring

* Real-time heart rate sensor reading.
* Store heart rate data.
* Alerts if abnormal levels detected.

---

## ✅ Step 4: Build from Small → Big

Now we build each small module and then **integrate them together**.

1. **Start with Heart Rate Module** → connect to a heart rate sensor (e.g., smartwatch).
2. **Add Physical Activity Module** → use phone/smartwatch accelerometer to track steps.
3. **Add Sleep Module** → log sleep manually or detect with wearable sensors.
4. **Integrate Modules** →

   * Combine all data into a **central dashboard**.
   * Store data in a database.
   * Generate overall health reports.

---

## ✅ Step 5: Explain Why Bottom-Up is Appropriate

* Each feature (heart rate, activity, sleep) is **independent** → easier to test one by one.
* Developers can work in **parallel** (one builds sleep tracker, another builds heart rate monitor).
* Flexibility: we can release a **basic version early** (e.g., only activity tracking) and add more features later.

---

## 📌 TL;DR

With **bottom-up**, we **start small** by building the **modules first** (heart rate, activity, sleep), test them separately, and then **combine them into a complete health monitoring system**. This works best when you know the features but not the entire design upfront.
