
# Actividad 4.2 – Pruebas de Software - Ejercicio de Programación 1

## P3 - Word Count
This project implements the **Word Count** program requested in *Actividad 4.2*. 

## Description 
The program reads a text file containing one word per line and calculates the frequency of each word.

The results are displayed on screen and written to an output file, following the exact format specified by the assignment.

---

## Program Requirements
The implementation satisfies the following requirements:

- The program is executed from the command line.
- The program receives a text file as a parameter.
- Each line in the file contains a word.
- Word counting is case-insensitive.
- The program detects and handles blank or invalid lines.
- Words are ordered by frequency in descending order.
- Ties are resolved using the order of first appearance in the input file.
- Results are displayed on screen and written to a results file.
- The total number of valid words is reported.
- Execution time is calculated and displayed.
- The program complies with **PEP 8** coding standards.
- Static analysis is performed using **pylint**.

---

## Execution
```bash
!python wordCount.py TC1.txt
