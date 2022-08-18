import os
from pwd import getpwuid

def find_owner(filename):
    return getpwuid(stat(filename).st_uid).pw_name

file_dir = ""
os.chdir(file_dir)
print(os.getcwd())

file_name = input('Enter File Name')

print(find_owner(file_name))


with open(file_name) as file:
    data =file.read()


