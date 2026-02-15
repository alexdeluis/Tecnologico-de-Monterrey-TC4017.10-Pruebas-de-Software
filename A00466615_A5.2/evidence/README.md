# Evidence Folder

This folder contains execution screenshots and static analysis reports for Activity 5.2.

Files included:
- execution_TC1.png
- execution_TC2.png
- execution_TC3.png
- flake8_initial.png
- flake8_report.txt
- flake8_clean.png
- flake8_clean_report.txt
- pylint_initial.png
- pylint_report.txt
- SalesResults_TC1.txt

## Notes on Test Cases

TC1 results match the expected Results.txt file.

TC2 and TC3 include invalid data such as:
- Negative quantities
- Products not found in catalog

These entries are ignored according to requirement 3,
therefore totals may differ from the provided reference file.

## Flake 8 Note

Flake8 clean report added after resolving E501 and W292 violations.

## Pylint Naming Convention Note

Pylint reports a naming convention warning (C0103) because the file name
computeSales.py does not follow snake_case style.

However, the assignment explicitly requires the program to be named
"computeSales.py", therefore the warning is intentionally accepted.
