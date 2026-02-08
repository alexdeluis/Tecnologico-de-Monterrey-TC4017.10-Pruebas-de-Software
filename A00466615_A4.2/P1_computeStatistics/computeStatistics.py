"""
computeStatistics.py

Computes basic statistics (mean, median, mode, variance, standard deviation)
from a file containing one number per line.

Author: Alejandro de Luis
"""

# pylint: disable=too-many-locals, too-many-branches

import sys
import time

def main():
    """Main execution function."""
    start_time = time.time()

    if len(sys.argv) != 2:
        print("Usage: python computeStatistics.py <input_file>")
        return

    file_name = sys.argv[1]
    numbers = []

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                try:
                    number = float(line.strip())
                    numbers.append(number)
                except ValueError:
                    print(
                        f"Invalid data at line {line_number}: "
                        f"{line.strip()}"
                    )
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return

    if not numbers:
        print("No valid numeric data found.")
        return

    #Count
    count = len(numbers)
    print(f"Count: {count}")

    #Mean
    total_sum = 0.0
    for value in numbers:
        total_sum += value

    mean = total_sum / count
    print(f"Mean: {mean}")

    #Median
    sorted_numbers = sorted(numbers)
    if count % 2 != 0:
        median = sorted_numbers[count // 2]
    else:
        middle1 = sorted_numbers[(count // 2) - 1]
        middle2 = sorted_numbers[count // 2]
        median = (middle1 + middle2) / 2

    print(f"Median: {median}")

    #Mode
    frequency = {}
    for value in numbers:
        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1

    max_frequency = max(frequency.values())

    if max_frequency == 1:
        mode = "#N/A"
    else:
        modes = []
        for key, freq in frequency.items():
            if freq == max_frequency:
                modes.append(key)
        mode = modes[0]  # tomar una si hay varias

    print(f"Mode: {mode}")

    #Variance
    variance_sum = 0.0
    for value in numbers:
        variance_sum += (value - mean) ** 2

    variance = variance_sum / count
    print(f"Variance: {variance}")

    #Standard Deviation
    standard_deviation = variance ** 0.5
    print(f"Standard Deviation: {standard_deviation}")

    #Elapsed Time
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time Elapsed: {elapsed_time:6f} seconds")

    with open("StatisticsResults.txt", "w", encoding="utf-8") as output_file:
        output_file.write(f"Count: {count}\n")
        output_file.write(f"Mean: {mean}\n")
        output_file.write(f"Median: {median}\n")
        output_file.write(f"Mode: {mode}\n")
        output_file.write(f"Variance: {variance}\n")
        output_file.write(
            f"Standard Deviation: {standard_deviation}\n"
        )
        output_file.write(
            f"Time Elapsed: {elapsed_time} seconds\n"
        )

if __name__ == "__main__":
    main()
    