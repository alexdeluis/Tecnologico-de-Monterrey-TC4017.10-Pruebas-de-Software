# Activity 5.2 – Static and Dynamic Testing

## Author: Alejandro de Luis - A00466615  
## Course: TC4017.10 – Software Testing  

---

# 1. Program Description

The program `computeSales.py` calculates the total cost of sales based on:

- A product price catalog (JSON file)
- A sales record file (JSON file)

The program:

- Is executed from the command line
- Handles invalid data without stopping execution
- Prints results on screen
- Generates a `SalesResults.txt` file
- Includes execution time
- Complies with PEP8
- Was validated using static analysis tools (flake8 and pylint)

---

# 2. How to Execute

```bash
python computeSales.py TC1.ProductList.json TC1.Sales.json
