"""
convert_numbers.py

A script that reads numbers from a file, converts them to binary and hexadecimal,
and saves the results.
"""

import sys
import time

def read_numbers_from_file(filename):
    """
    Reads numbers from a file, ignoring invalid entries.

    Args:
        filename (str): The name of the file to read numbers from.

    Returns:
        list: A list of valid integers from the file.
    """
    numbers = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:  # Specify encoding
            for line in file:
                try:
                    numbers.append(int(line.strip()))
                except ValueError:
                    print(f"Invalid data found and skipped: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    except OSError as e:  # More specific exception
        print(f"An error occurred while accessing the file: {e}")
        sys.exit(1)
    return numbers

def convert_to_binary(number):
    """
    Converts a given integer to its binary representation.

    Args:
        number (int): The number to convert.

    Returns:
        str: The binary representation of the number.
    """
    return bin(number)[2:]  # Uses built-in bin() function to simplify conversion

def convert_to_hexadecimal(number):
    """
    Converts a given integer to its hexadecimal representation.

    Args:
        number (int): The number to convert.

    Returns:
        str: The hexadecimal representation of the number.
    """
    return hex(number)[2:].upper()  # Uses built-in hex() function and formats output

def write_results_to_file(filename, results):
    """
    Writes the conversion results to a file.

    Args:
        filename (str): The name of the file to write results.
        results (list): A list of formatted result strings.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:  # Specify encoding
            for result in results:
                file.write(result + "\n")
    except OSError as e:  # More specific exception
        print(f"An error occurred while writing to the file: {e}")

def main():
    """
    Main function that reads numbers, converts them, and saves the results.
    """
    if len(sys.argv) != 2:
        print("Usage: python convert_numbers.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    start_time = time.time()

    numbers = read_numbers_from_file(filename)
    if not numbers:
        print("No valid numbers found in the file.")
        sys.exit(1)

    results = []
    for num in numbers:
        binary = convert_to_binary(num)
        hexadecimal = convert_to_hexadecimal(num)
        result = f"Number: {num}, Binary: {binary}, Hexadecimal: {hexadecimal}"
        print(result)
        results.append(result)

    end_time = time.time()
    elapsed_time = end_time - start_time

    results.append(f"Execution Time (seconds): {elapsed_time}")
    print(f"Execution Time (seconds): {elapsed_time}")

    write_results_to_file("ConversionResults.txt", results)
    print("Results saved in ConversionResults.txt")

if __name__ == "__main__":
    main()
