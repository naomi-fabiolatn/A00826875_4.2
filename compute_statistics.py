"""
compute_statistics.py

A script that reads numbers from a file, computes statistical measures (mean, median,
mode, variance, standard deviation), and saves the results.
"""

import sys
import time

def read_numbers_from_file(filename):
    """
    Reads numbers from a file, ignoring invalid entries.

    Args:
        filename (str): The name of the file to read numbers from.

    Returns:
        list: A list of valid float numbers from the file.
    """
    numbers = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:  # Specify encoding
            for line in file:
                try:
                    numbers.append(float(line.strip()))
                except ValueError:
                    print(f"Invalid data found and skipped: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    except OSError as e:  # More specific exception
        print(f"An error occurred while accessing the file: {e}")
        sys.exit(1)
    return numbers

def calculate_mean(numbers):
    """
    Calculates the mean (average) of a list of numbers.

    Args:
        numbers (list): List of numbers.

    Returns:
        float: The mean value.
    """
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    """
    Calculates the median of a list of numbers.

    Args:
        numbers (list): List of numbers.

    Returns:
        float: The median value.
    """
    numbers.sort()
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]
    mid1, mid2 = numbers[n // 2 - 1], numbers[n // 2]
    return (mid1 + mid2) / 2

def calculate_mode(numbers):
    """
    Calculates the mode of a list of numbers.

    Args:
        numbers (list): List of numbers.

    Returns:
        float or list: The mode (most frequent number) or multiple modes.
    """
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    mode = [num for num, freq in frequency.items() if freq == max_freq]
    return mode[0] if len(mode) == 1 else mode

def calculate_variance(numbers, mean):
    """
    Calculates the variance of a list of numbers.

    Args:
        numbers (list): List of numbers.
        mean (float): The mean of the numbers.

    Returns:
        float: The variance.
    """
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def calculate_standard_deviation(variance):
    """
    Calculates the standard deviation from the variance.

    Args:
        variance (float): The variance.

    Returns:
        float: The standard deviation.
    """
    return variance ** 0.5

def write_results_to_file(filename, results):
    """
    Writes the statistical results to a file.

    Args:
        filename (str): The name of the file to write results.
        results (dict): A dictionary of statistical measures.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:  # Specify encoding
            for key, value in results.items():
                file.write(f"{key}: {value}\n")
    except OSError as e:  # More specific exception
        print(f"An error occurred while writing to the file: {e}")

def main():
    """
    Main function that reads numbers, calculates statistics, and saves the results.
    """
    if len(sys.argv) != 2:
        print("Usage: python compute_statistics.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    start_time = time.time()

    numbers = read_numbers_from_file(filename)
    if not numbers:
        print("No valid numbers found in the file.")
        sys.exit(1)

    mean = calculate_mean(numbers)
    median = calculate_median(numbers)
    mode = calculate_mode(numbers)
    variance = calculate_variance(numbers, mean)
    std_dev = calculate_standard_deviation(variance)

    end_time = time.time()
    elapsed_time = end_time - start_time

    results = {
        "Mean": mean,
        "Median": median,
        "Mode": mode,
        "Variance": variance,
        "Standard Deviation": std_dev,
        "Execution Time (seconds)": elapsed_time
    }

    for key, value in results.items():
        print(f"{key}: {value}")

    write_results_to_file("StatisticsResults.txt", results)
    print("Results saved in StatisticsResults.txt")

if __name__ == "__main__":
    main()
