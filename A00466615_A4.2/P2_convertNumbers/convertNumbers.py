"""
convertNumbers.py

Reads integers from a file and converts each valid number to
binary and hexadecimal representations.

Author: Alejandro de Luis
"""

# pylint: disable=invalid-name

import sys
import time


def main():
    """Main execution function."""
    start_time = time.time()

    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py <input_file>")
        return

    file_name = sys.argv[1]
    valid_numbers = []

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                value = line.strip()

                try:
                    number = int(value)
                    valid_numbers.append(number)
                except ValueError:
                    print(
                        f"Invalid data at line {line_number}: {value}"
                    )
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return

    if not valid_numbers:
        print("No valid integer data found.")
        return

    print(f"Valid integers count: {len(valid_numbers)}")

    print("\nConversions:")
    for number in valid_numbers:
        binary_value = bin(number)[2:]
        hex_value = hex(number)[2:].upper()

        print(
        f"Decimal: {number} | "
        f"Binary: {binary_value} | "
        f"Hexadecimal: {hex_value}"
      )

    end_time = time.time()
    elapsed_time = end_time - start_time

    output_file_name = "convertNumbers/ConversionResults_TC4.txt"
    with open(output_file_name, "w", encoding="utf-8") as output_file:
        output_file.write(
            f"Valid integers count: {len(valid_numbers)}\n\n"
        )
        output_file.write("Conversions:\n")

        for number in valid_numbers:
            binary_value = bin(number)[2:]
            hex_value = hex(number)[2:].upper()

            output_file.write(
                f"Decimal: {number} | "
                f"Binary: {binary_value} | "
                f"Hexadecimal: {hex_value}\n"
            )

        output_file.write(
            f"\nTime Elapsed: {elapsed_time} seconds\n"
        )

if __name__ == "__main__":
    main()
