"""
read first n lines of file, filename is passed as script argument
"""

import sys

NUMBER_LINES = 4

if len(sys.argv) != 2:
    print("Only filename needed!")
    quit()

try:
    file = open(sys.argv[1], "r", encoding="utf-8")
    line = file.readline()
    count = 0
    while count < NUMBER_LINES and line != "":
        line = line.strip()
        count += 1
        print(line)
        line = file.readline()
    file.close()
except OSError as err:
    print(f"Error accesing file: {err}")
