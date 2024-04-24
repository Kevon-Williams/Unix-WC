import os
import argparse


def main():
    # Initialize the argument parser with a brief description
    parser = argparse.ArgumentParser(description="Command-line tool for file operations.")

    # Define the command-line arguments
    parser.add_argument('-a', '--all', type=str, help="Calculate and return the number of lines, words, and the size of a file in bytes.")
    parser.add_argument('-c', '--characters', type=str, help="Return the size of a file in bytes (characters).")
    parser.add_argument('-l', '--lines', type=str, help="Return the number of lines in a file.")
    parser.add_argument('-w', '--words', type=str, help="Return the number of words in a file.")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Fetch the user inputs for various operations
    filename_chars = args.characters
    filename_lines = args.lines
    filename_words = args.words
    filename_all = args.all

    # Process based on user input
    if filename_chars:
        print(f"'{filename_chars}' has {get_file_size(filename_chars)} bytes.")

    if filename_lines:
        print(f"'{filename_lines}' has {get_file_lines(filename_lines)} lines.")

    if filename_words:
        print(f"'{filename_words}' has {get_file_words(filename_words)} words.")

    # calculate all details for a given file
    if filename_all:
        num_lines = get_file_lines(filename_all)
        num_words = get_file_words(filename_all)
        num_bytes = get_file_size(filename_all)

        print(f"'{filename_all}' has {num_lines} lines, {num_words} words, and {num_bytes} bytes.")


def get_file_size(filepath):
    """Returns the size of the file in bytes."""
    with open(filepath, 'r', errors="ignore") as file:
        file.seek(0, os.SEEK_END)  # Move to the end of the file
        return file.tell()  # Return the position, which is equivalent to the file size


def get_file_lines(filepath):
    """Returns the number of lines in the file."""
    line_count = 0
    with open(filepath, 'r', errors="ignore") as file:
        for _ in file:
            line_count += 1
    return line_count


def get_file_words(filepath):
    """Returns the number of words in the file."""
    word_count = 0
    with open(filepath, 'r', errors="ignore") as file:
        text = file.read()  # Read the entire content
        word_count = len(text.split())  # Count words by splitting
    return word_count


if __name__ == "__main__":
    main()
