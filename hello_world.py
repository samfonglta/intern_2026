import csv
import os

text = "Hello, World!"
dir = os.listdir("dataset")

for file in dir:
    with open(os.path.join("dataset", file), "w") as f:
        f.write(text)

