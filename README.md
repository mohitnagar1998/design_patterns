# 🎯 Design Patterns in Python

This repository contains Python implementations of various **Object-Oriented Design Patterns**, each accompanied by a **UML-style diagram** and **example code** to demonstrate real-world usage.

The goal of this project is to provide **clear, practical, and easy-to-understand examples** for mastering design patterns in Python.

---

## 🧩 Implemented Patterns

| Pattern | Category | Description |
|----------|-----------|-------------|
| [Abstract Factory](./AbstractFactoryPattern) | Creational | Provides an interface for creating families of related or dependent objects without specifying their concrete classes. |
| [Factory Method](./FactoryPattern) | Creational | Defines an interface for creating an object but lets subclasses decide which class to instantiate. |
| [Decorator](./DecoratorPattern) | Structural | Allows adding new functionality to objects dynamically without modifying their structure. |
| [Proxy](./ProxyDesignPattern) | Structural | Provides a surrogate or placeholder for another object to control access to it. |
| [Observer](./ObserverPattern) | Behavioral | Defines a one-to-many dependency between objects so that when one changes state, all dependents are notified. |
| [Chain of Responsibility](./ChainOfResponsibilityPattern) | Behavioral | Passes requests along a chain of handlers, where each handler decides either to process the request or pass it along. |
| [Strategy](./StrategyPattern) | Behavioral | Defines a family of algorithms, encapsulates each one, and makes them interchangeable at runtime. |

---

## 🧠 Project Structure

```
design_patterns/
│
├── AbstractFactoryPattern/
│   ├── abstract_factory.py
│   ├── diagram.png
│   └── README.md
│
├── ChainOfResponsibilityPattern/
│   ├── chain_of_responsibility.py
│   ├── diagram.png
│   └── README.md
│
├── DecoratorPattern/
│   ├── decorator.py
│   ├── diagram.png
│   └── README.md
│
├── FactoryPattern/
│   ├── factory.py
│   ├── diagram.png
│   └── README.md
│
├── ObserverPattern/
│   ├── observer.py
│   ├── diagram.png
│   └── README.md
│
├── ProxyDesignPattern/
│   ├── proxy.py
│   ├── diagram.png
│   └── README.md
│
├── StrategyPattern/
│   ├── strategy.py
│   ├── diagram.png
│   └── README.md
│
└── README.md
```

Each pattern folder contains:
- 🧠 **Pattern code implementation**
- 🧩 **Diagram explaining the pattern**
- 📘 **README** explaining the concept, when to use it, and code walkthrough

---

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/mohitnagar1998/design_patterns.git
   ```
2. Navigate to a specific pattern directory:
   ```bash
   cd design_patterns/StrategyPattern
   ```
3. Run the example:
   ```bash
   python strategy.py
   ```

---

## 🖼️ Diagrams

Each pattern includes a clear UML-style diagram showing:
- Key classes/interfaces
- Relationships (inheritance, composition, etc.)
- Execution flow


---

## 💡 Future Plans

- Add remaining **Creational**, **Structural**, and **Behavioral** patterns  
- Include **real-world use cases** for each pattern  
- Add **unit tests** for all patterns  

---

## 🧰 Tools & Technologies

- **Python 3.10+**
- **PyCharm** for development
- **draw.io / Lucidchart** for diagrams

---

## 📚 References

- *Design Patterns: Elements of Reusable Object-Oriented Software* – Erich Gamma et al.

---

## 👨‍💻 Author

**Mohit Nagar**  
Software Engineer @ Venera Technologies  
[LinkedIn](https://www.linkedin.com/in/mohitnagar1998/) • [GitHub](https://github.com/mohitnagar1998) • [LeetCode](https://leetcode.com/u/mohitnagar1998/)

---

🧱 *“Good design is invisible — it just works.”*
