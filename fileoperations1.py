import os

#input file location in file_path

file_path = ""
os.chdir(file_path)
print(os.getcwd())
l1 = []
l2 = []
#input file name
file_name = ""
with open(file_name) as file:
    data =file.read()
    for line in data:
        l1 = line.split()
print(l1)

