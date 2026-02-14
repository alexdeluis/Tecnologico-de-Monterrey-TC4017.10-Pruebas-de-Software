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
    """
    Load and return JSON data from a file.

    Args:
        filepath (str): Path to the JSON file.

    Returns:
        list | dict | None: Parsed JSON content or None if error occurs.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")

    except json.JSONDecodeError:
        print(f"Error: File '{filepath}' contains invalid JSON.")

    except OSError as error:
        print(f"OS error while reading '{filepath}': {error}")

    return None


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

    print("Files loaded successfully.")

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Execution time: {elapsed_time:.4f} seconds")


if __name__ == "__main__":
    main()
