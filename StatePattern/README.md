
# State Design Pattern

## Overview
The **State Pattern** is a behavioral design pattern that allows an object to change its behavior when its internal state changes.
The object appears to change its class by delegating behavior to state objects.

---

## Problem
When behavior depends on state, developers often use `if/else` or `switch` statements:

- Code becomes cluttered with conditionals
- Adding new states is difficult
- Logic is hard to maintain and extend

---

## Solution (State Pattern)
Encapsulate each state as a separate class and delegate behavior to the current state object.
Changing behavior means switching the state object, not modifying logic.

---

## Structure
- **Context** – Holds the current state
- **State Interface** – Defines common behavior
- **Concrete States** – Implement state-specific behavior

---

## Real-World Example
**Traffic Light System**
- Red → Stop
- Yellow → Ready
- Green → Go

The same signal behaves differently based on its state.

---

## Code Examples
This folder contains:
- Traffic Light implementation **without** State Pattern (using conditionals)
- Traffic Light implementation **with** State Pattern (using state classes)

---

## Benefits
- Removes complex conditional logic
- Improves readability and maintainability
- Easy to add new states
- Follows Open/Closed Principle

---

## Drawbacks
- Increases number of classes
- Slight overhead for very simple state logic

---

## When to Use
- Behavior depends on state
- States change frequently at runtime
- Conditional logic is growing

---

## One-Line Summary
> The **State Pattern** allows an object to change its behavior by changing its internal state object.
