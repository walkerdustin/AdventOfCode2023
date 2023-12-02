import numpy as np
import pandas as pd

# import the input from txt file
list_of_lines = []
with open("input.txt") as fp:
    for line in fp:
        list_of_lines.append(line.strip().split("\t"))
print(list_of_lines)
print(len(list_of_lines))
# remove all chars from the input list_of_lines
alphabet = "abcdefghijklmnopqrstuvwxyz"
line.translate({ord(i): None for i in "abc"})
