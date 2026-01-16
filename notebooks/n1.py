# This program works like the Unix 'nl' command.
# It prints each line of a text file with a line number in front.

import sys

# Make sure the user provided a file name
if len(sys.argv) != 2:
    print("Usage: python nl.py <filename>")
    sys.exit()

filename = sys.argv[1]

try:
    # Open the file safely
    with open(filename, "r") as file:
        line_number = 1

        # Read the file line by line
        for line in file:
            # Print the line number followed by the line content
            print(f"{line_number}: {line}", end="")
            line_number += 1

except FileNotFoundError:
    print("Error: File not found.")
