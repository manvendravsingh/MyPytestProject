import csv
import os
from pathlib import Path
file_name = "\\_Test_deviceList.csv"
downloads_path = str(Path.home() / "Downloads") + file_name

print(downloads_path)
try:
    if os.path.exists(downloads_path):
        print("Cleaning the directory for Testing")
        os.remove(downloads_path)
except Exception as e:
    print(str(e))
# f = open(downloads_path, "r")
# print(f.readlines())
#
# # for line in f.readlines():
#
# with open(downloads_path, "r") as exportCSV:
#     data = csv.reader(exportCSV)
#     next(data, None)
#     for row in data:
#         print(row[4])
#     # for index, row in enumerate(data):
#     #     if index > 1:
#     #         print(row[4])
#
