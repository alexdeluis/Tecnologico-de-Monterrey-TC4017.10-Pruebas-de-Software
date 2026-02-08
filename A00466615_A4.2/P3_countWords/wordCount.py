"""
wordCount.py

Reads a text file containing words (one per line) and counts
the frequency of each word.

Results are displayed on screen and written to an output file.

Author: Alejandro de Luis
"""

# pylint: disable=invalid-name, too-many-locals

import sys
import time


def main():
    """Main execution function."""
    start_time = time.time()

    if len(sys.argv) != 2:
        print("Usage: python wordCount.py <input_file>")
        return

    file_name = sys.argv[1]

    word_counts = {}
    blank_count = 0
    total_words = 0

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for line in file:
                word = line.strip().lower()

                if not any(char.isalpha() for char in word):
                    blank_count += 1
                else:
                    total_words += 1
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return

    sorted_words = sorted(
        word_counts.items(),
        key=lambda item: item[1],
        reverse=True
    )

    input_base_name = file_name.split("/")[-1].replace(".txt", "")
    output_file_name = f"WordCountResults_{input_base_name}.txt"

    # Encabezado
    header = f"Row Labels\tCount of {input_base_name}"

    print(header)

    with open(output_file_name, "w", encoding="utf-8") as output_file:
        output_file.write(header + "\n")

        for word, count in sorted_words:
            print(f"{word}\t{count}")
            output_file.write(f"{word}\t{count}\n")

        # Blank (si existe)
        if blank_count > 0:
            print("(blank)")
            output_file.write("(blank)\n")

        # Grand Total
        print(f"Grand Total\t{total_words}")
        output_file.write(f"Grand Total\t{total_words}\n")

        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f"\nTime Elapsed: {elapsed_time} seconds")
        output_file.write(
            f"\nTime Elapsed: {elapsed_time} seconds\n"
        )


if __name__ == "__main__":
    main()
