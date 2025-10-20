
# Command-Line Calculator

## Overview

This is a **simple command-line calculator** written in Python. It allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division. Users can continue calculations with the previous result, start a new calculation, or exit the program.

It is fully **interactive** and handles invalid inputs and division by zero gracefully.

---

## Features

* Supports operations by **symbols** (`+`, `-`, `*`, `/`) or **words** (`add`, `subtract`, `multiply`, `division`).
* Allows **continuous calculations** using the previous result.
* Starts **new calculations** without restarting the program.
* Prevents **division by zero** errors.
* Validates all inputs to ensure only numbers and correct operations are used.

---

## Requirements

* Python 3.x
* Runs on any terminal or command prompt (Windows, macOS, Linux)

---

## Usage

1. **Run the program**:

   ```bash
   python calculator.py
   ```

2. **Enter the first number** when prompted.

3. **Enter the second number** when prompted.

4. **Choose an operation**:

   * Symbols: `+`, `-`, `*`, `/`
   * Words: `add`, `subtract`, `multiply`, `division`

5. **View the result**.

6. **Choose what to do next**:

   * `C` → Continue calculation with the current result
   * `N` → Start a new calculation
   * `E` → Exit the program

---

## Example

```
Enter first number: 10
Enter second number: 5
Available operations: +, -, *, / or add, subtract, multiply, division
Enter operation: +
Result: 15.0
Continue with result (C), new calculation (N), or exit (E)? C
Enter second number: 3
Enter operation: multiply
Result: 45.0
Continue with result (C), new calculation (N), or exit (E)? E
```

---

## Notes

* If the user attempts to divide by zero, the program will ask for a **new number** instead of crashing.
* Invalid inputs (like letters instead of numbers) are **rejected with a message** prompting re-entry.

---
