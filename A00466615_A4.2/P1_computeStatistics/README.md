# Actividad 4.2 – Pruebas de Software - Ejercicio de Programación 1

## P1 – Compute Statistics

This repository contains the implementation of the **Compute Statistics**
program developed in Python, following the requirements specified in
Actividad 4.2.

### Description
The program reads a text file containing one value per line and computes
the following statistics using basic algorithms (no statistical libraries):

- Count
- Mean
- Median
- Mode
- Variance
- Standard Deviation

The program also detects and reports invalid data without interrupting
execution.

## Program Requirements
The implementation satisfies the following requirements:

- The program is executed from the command line.
- The program receives a text file as a parameter.
- The input file contains numeric values, one per line.
- The program computes the following statistics for the valid data:
  - Count
  - Mean
  - Median
  - Mode
  - Variance
  - Standard Deviation
- Invalid data is detected, reported in the console, and does not stop the execution.
- The program processes files containing hundreds of numeric values.
- Results are displayed on the screen and written to an output file.
- The total execution time is calculated and displayed.
- The program follows **PEP 8** coding standards.
- Static code analysis is performed using **pylint**.

---

### Execution
```bash
!python computeStatistics.py TC1.txt

