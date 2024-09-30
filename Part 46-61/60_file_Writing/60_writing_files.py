#  Python Writing files (.txt, .json, .csv)

import json
import csv

txt_data = "I like The Pizza!!"

# file_path = "output.txt"
# employees = ["Bhavik","Axit","Dhruv","Vishv"]

# file_path = "output.json"
# it is for json file
# employee = {
#             "name": "Bhavik",
#             "age" : "19",
#             "job" : "Student"}

file_path = "output.csv"
employees = [["Name","Age","Job"],
                   ["Bhavik","18","Study"],
                   ["Axit","24","intern"],
                   ["SRK","55","Actor"]]

try:
    with open(file=file_path, mode="w", newline="") as file:
        # file.write(txt_data)
        # for employee in employees:
        #     file.write(employee + "\n")
        # print(f"The File {file_path} had been created!!")
        
        # json.dump(employee,file,indent=4)
        # print(f"Json File {file_path} had been created!!")
        
        writer =  csv.writer(file)
        for row in employees:
            writer.writerow(row)
        
        print(f"CSV File {file_path} had been created!!")
        
except FileExistsError:
    print(f"The {file_path} File already exist!!")
     
# mode: x = write (if file doesn't exist)
#       a = append (add text in the file)
