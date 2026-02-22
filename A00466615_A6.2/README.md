# Activity A6.2 – Unit Testing and Software Quality

## Author: Alejandro de Luis
## Course: TC4017 - Software Testing

## 📌 Overview

This project implements a Hotel management system in Python following:

- Test-Driven Development (TDD)
- Unit testing with `unittest`
- JSON persistence
- Defensive programming practices
- Static code analysis (flake8 & pylint)
- Code coverage measurement

The objective is to demonstrate best practices in unit testing, error handling, and software quality assurance.

---

## 🏗 Project Structure


---

## 🧠 Features Implemented

### Hotel Class
- Input validation on initialization
- Room reservation management
- Reservation cancellation
- JSON-based persistence
- Handling of corrupted JSON files
- Error handling without interrupting execution

---

## 🧪 Unit Tests

Implemented using Python's `unittest` framework.

### Test Coverage Includes:

- Valid hotel creation
- 5+ negative test cases (invalid inputs)
- Room reservation logic
- Reservation cancellation logic
- JSON save functionality
- JSON load functionality
- Handling of corrupted JSON files

Total tests: **14**

---

## 📊 Code Quality Metrics

### Coverage

## 🚀 How to Run Tests

From the project root:

```bash
python3 -m unittest discover -s tests

To run coverage:
```bash
python3 -m coverage run -m unittest discover -s tests
python3 -m coverage report -m

To run flake:
```bash
python3 -m flake8 .

To run pylint:
```bash
python3 -m pylint .