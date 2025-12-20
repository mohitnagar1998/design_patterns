# Null Object Design Pattern

## Overview
The **Null Object Pattern** is a behavioral design pattern that replaces `null` (or `None`) references with a special object that provides **default, do-nothing behavior**.
This eliminates repeated null checks and makes client code safer and cleaner.

---

## Problem
In many applications, objects may be optional. The common approach is to return `null` and guard every call with checks:

```python
if notifier is not None:
    notifier.send("Order placed")
```

### Issues with this approach:
- Too many conditional checks
- Error-prone (easy to forget a check)
- Messy and hard-to-maintain code
- Violates clean OOP design principles

---

## Solution (Null Object Pattern)
Instead of returning `null`, return a **Null Object** that:
- Implements the same interface
- Performs no action (safe default behavior)

Client code always works with an object and never needs to check for `null`.

---

## Structure
- **Interface / Abstract Class** – defines expected behavior
- **Real Object** – performs actual logic
- **Null Object** – provides empty or default behavior
- **Factory (optional)** – decides which object to return

---

## Example

### Without Null Object Pattern
```python
notifier = get_notifier(enabled=False)

if notifier is not None:
    notifier.send("Order placed")
```

### With Null Object Pattern
```python
notifier = get_notifier(enabled=False)
notifier.send("Order placed")  # Safe, no check needed
```

---

## Benefits
- Eliminates null checks
- Prevents runtime errors
- Cleaner and more readable code
- Leverages polymorphism
- Improves maintainability

---

## When to Use
- Missing object is a valid scenario
- Default behavior is acceptable
- You want to avoid repetitive null checks

---

## When Not to Use
- Absence of object represents an error
- Silent failure can hide bugs
- Explicit handling is required

---

## One-Line Summary
> The **Null Object Pattern** replaces `null` references with an object that provides default behavior, simplifying code and avoiding null-related errors.


