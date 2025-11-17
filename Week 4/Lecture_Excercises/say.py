import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("hello " + sys.argv[1])

# program to print an ASCII art after an argument in command-line
