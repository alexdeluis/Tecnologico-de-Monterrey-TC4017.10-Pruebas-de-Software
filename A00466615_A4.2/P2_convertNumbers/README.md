# Actividad 4.2 – P2: Converter - Ejercicio de Programación 1

## Description
This project implements the **Converter** program requested in *Actividad 4.2*.  
The program reads a file containing numeric values and converts each valid number to its **binary** and **hexadecimal** representation.

All computations are performed using **basic algorithms only**, without relying on specialized libraries, in compliance with the assignment requirements.

---

## Program Requirements
The implementation satisfies the following requirements:

- The program is invoked from the command line.
- The program receives a file as a parameter.
- The file contains a list of items (presumable numbers).
- Each valid number is converted to:
  - Binary base
  - Hexadecimal base
- Results are displayed on the screen and written to an output file.
- Invalid data is detected, reported in the console, and execution continues.
- The program handles files with hundreds or thousands of items.
- The execution time is calculated and displayed.
- The program follows **PEP 8** coding standards.
- Static code analysis was performed using **pylint**.

---

## Execution
```bash
!python convertNumbers/convertNumbers.py convertNumbers/TC1.txt

