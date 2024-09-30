#  Python Writing files (.txt, .json, .csv)

import json
import csv

# file_path = "input.txt"
# file_path = "input.json"
file_path = "input.csv"

try:
    with open (file=file_path,mode="r") as file:
        # content = file.read()
        # content = json.load(file)
        content = csv.reader(file)
        for line in content:
            print(line[0])
except FileNotFoundError:
    print(f"The Given {file_path} doesn't Exist.")
except PermissionError:
    print(f"the permission denied for {file_path}")
    