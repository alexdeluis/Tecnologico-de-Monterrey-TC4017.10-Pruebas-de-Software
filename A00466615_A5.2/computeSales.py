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


def main():
    """Main function to control program execution."""
    if len(sys.argv) != 3:
        print("Usage: python computeSales.py priceCatalogue.json salesRecord.json")
        sys.exit(1)

    price_file = sys.argv[1]
    sales_file = sys.argv[2]

    start_time = time.time()

    # Placeholder logic (to be implemented step by step)
    print("Program started...")
    print(f"Price file: {price_file}")
    print(f"Sales file: {sales_file}")

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Execution time: {elapsed_time:.4f} seconds")


if __name__ == "__main__":
    main()
