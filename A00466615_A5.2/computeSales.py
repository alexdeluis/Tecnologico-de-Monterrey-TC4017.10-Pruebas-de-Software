"""
computeSales.py

Program to compute total sales from a product catalogue
and a sales record file in JSON format.

Usage:
    python computeSales.py priceCatalogue.json salesRecord.json

Author: Alejandro de Luis
"""

import sys
import json
import time


def load_json_file(filepath):
    """Load and return JSON data from a file."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")

    except json.JSONDecodeError:
        print(f"Error: File '{filepath}' contains invalid JSON.")

    except OSError as error:
        print(f"OS error while reading '{filepath}': {error}")

    return None


def build_price_catalog(product_list):
    """Build dictionary mapping product titles to prices."""
    catalog = {}

    for product in product_list:
        try:
            title = product["title"]
            price = product["price"]
            catalog[title] = price
        except KeyError as error:
            print(f"Missing key in product entry: {error}")

    return catalog


def compute_total_sales(sales_data, catalog):
    """Compute total cost of sales."""
    total = 0.0

    for record in sales_data:
        try:
            product_name = record["Product"]
            quantity = record["Quantity"]

            if quantity <= 0:
                print(
                    f"Invalid quantity for product "
                    f"'{product_name}': {quantity}"
                )
                continue

            if product_name not in catalog:
                print(f"Product not found in catalog: '{product_name}'")
                continue

            price = catalog[product_name]
            total += price * quantity

        except KeyError as error:
            print(f"Missing key in sales record: {error}")

    return total


def write_results(total, elapsed_time):
    """Write results to SalesResults.txt file."""
    filename = "SalesResults.txt"

    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("===== SALES SUMMARY =====\n")
            file.write(f"Total Sales: {total:.2f}\n")
            file.write(f"Execution time: {elapsed_time:.4f} seconds\n")

    except OSError as error:
        print(f"Error writing results file: {error}")


def main():
    """Main function to control program execution."""
    if len(sys.argv) != 3:
        print("Usage: python computeSales.py priceCatalogue.json salesRecord.json")
        sys.exit(1)

    price_file = sys.argv[1]
    sales_file = sys.argv[2]

    start_time = time.time()

    price_data = load_json_file(price_file)
    sales_data = load_json_file(sales_file)

    if price_data is None or sales_data is None:
        print("Program terminated due to file errors.")
        sys.exit(1)

    catalog = build_price_catalog(price_data)
    total_sales = compute_total_sales(sales_data, catalog)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("\n===== SALES SUMMARY =====")
    print(f"Total Sales: {total_sales:.2f}")
    print(f"Execution time: {elapsed_time:.4f} seconds")

    write_results(total_sales, elapsed_time)


if __name__ == "__main__":
    main()
