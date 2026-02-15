# Evidence Folder

This folder contains execution screenshots and static analysis reports for Activity 5.2.

Files included:
- execution_TC1.png
- execution_TC2.png
- execution_TC3.png
- flake8_report.txt
- pylint_report.txt

## Notes on Test Cases

TC1 results match the expected Results.txt file.

TC2 and TC3 include invalid data such as:
- Negative quantities
- Products not found in catalog

These entries are ignored according to requirement 3,
therefore totals may differ from the provided reference file.

Flake8 clean report added after resolving E501 and W292 violations.
