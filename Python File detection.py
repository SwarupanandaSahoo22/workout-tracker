# # Python File detection

# import os

# file_path = r"C:\Users\Acer\OneDrive\python\text.txt"

# if os.path.exists(file_path):
#     print(f"The location '{file_path}' exists")

# else:
#     print("The location doesn't exists")








# Python Writing Files (.txt, .json, .csv)

# 1.txt

# likes = ["I like biryani", "I love my girlfriend"]

# file_path = "C:/Users/Acer/OneDrive/python/text.txt"

# try:
#     with open(file_path, "w") as file:
#         for like in likes:
#             file.write(like + "\n")
#         print(f"txt file '{file_path}' was created")

# except FileExistsError:
#     print("That file already exists!")



# 2.json

# import json

# employee = {
#     "name": "Spongbob",
#     "age": 18,
#     "occupation": "cook"
# }

# file_path = "C:/Users/Acer/OneDrive/python/text.json"

# try:
#     with open(file_path, "w") as file:
#         json.dump(employee, file, indent=4)
#         print(f"json file '{file_path}' was created")

# except FileExistsError:
#     print("That file already exists!")


# 3.csv

# import csv

# employees = [["Name", "Age", "Job"],
#             ["Spongebob", 18, "Cook"], 
#             ["Squidward", 27, "Cashier"], 
#             ["Patrick", 19, "Janitor"]]

# file_path = "C:/Users/Acer/OneDrive/python/text.csv"

# try:
#     with open(file_path, "w", newline="") as file:
#         writer = csv.writer(file)
#         for row in employees:
#             writer.writerow(row)
#         print(f"csv file '{file_path}' was created")

# except FileExistsError:
#     print("That file already exists!")












# Python Reading Files (.txt, .json, .csv)

#1. txt

# file_path = "C:/Users/Acer/OneDrive/python/text.txt"

# try:
#     with open(file_path, "r") as file:
#         content = file.read()
#         print(content)

# except FileNotFoundError:
#     print("This file can not be found")
# except PermissionError:
#     print("You do not have the permission to read that file")



# 2.json

# import json
# file_path = "C:/Users/Acer/OneDrive/python/text.json"

# try:
#     with open(file_path, "r") as file:
#         content = json.load(file)
#         print(content["name"])
#         print(content["age"])
#         print(content["occupation"])

# except FileNotFoundError:
#     print("This file can not be found")
# except PermissionError:
#     print("You do not have the permission to read that file")



# 3.csv

import csv
file_path = "C:/Users/Acer/OneDrive/python/text.csv"

try:
    with open(file_path, "r") as file:
       content = csv.reader(file)
       for line in content:
        print(line)
except FileNotFoundError:
    print("This file can not be found")
except PermissionError:
    print("You do not have the permission to read that file")