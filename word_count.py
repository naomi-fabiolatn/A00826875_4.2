"""
word_count.py

A simple script to count word frequencies in a text file and save the results.
"""

import sys
import time

def read_words_from_file(filename):
    """
    Reads words from a given file and returns a list of words.

    Args:
        filename (str): The name of the file to read.

    Returns:
        list: A list of words extracted from the file.
    """
    words = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:  # Specify encoding
            for line in file:
                words.extend(line.strip().split())  # Split words by spaces
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
    except OSError as e:  # Catch OS-related file errors
        print(f"An error occurred while accessing the file: {e}")
        sys.exit(1)
    return words

def count_word_frequencies(words):
    """
    Counts the frequency of each word in a list.

    Args:
        words (list): List of words.

    Returns:
        dict: A dictionary with words as keys and their frequencies as values.
    """
    word_count = {}
    for word in words:
        word = word.lower()  # Convert to lowercase for case-insensitive matching
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def write_results_to_file(filename, results, elapsed_time):
    """
    Writes the word frequency results and execution time to a file.

    Args:
        filename (str): The name of the file to write results.
        results (dict): A dictionary with word frequencies.
        elapsed_time (float): The execution time of the script.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:  # Specify encoding
            for word, count in results.items():
                file.write(f"{word}: {count}\n")
            file.write(f"Execution Time (seconds): {elapsed_time}\n")
    except OSError as e:  # Catch OS-related file errors
        print(f"An error occurred while writing to the file: {e}")

def main():
    """
    Main function to execute the word counting script.
    """
    if len(sys.argv) != 2:
        print("Usage: python word_count.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    start_time = time.time()

    words = read_words_from_file(filename)
    if not words:
        print("No valid words found in the file.")
        sys.exit(1)

    word_frequencies = count_word_frequencies(words)

    end_time = time.time()
    elapsed_time = end_time - start_time

    for word, count in word_frequencies.items():
        print(f"{word}: {count}")
    print(f"Execution Time (seconds): {elapsed_time}")

    write_results_to_file("WordCountResults.txt", word_frequencies, elapsed_time)
    print("Results saved in WordCountResults.txt")

if __name__ == "__main__":
    main()
