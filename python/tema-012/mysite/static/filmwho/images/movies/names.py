import os
import sqlite3

# specify the directory path
path = "./"

# get all the files in the directory
files = os.listdir(path)

# # filter out all .webp files
files = [file for file in files if file.endswith(".webp")]

with open("../../../../names.txt", "w") as line:
    for item in files:
        line.write("images/posters/{0}\n".format(item))