import os
from os.path import expanduser

home_directory = expanduser("~")
print(home_directory)

print(os.getcwd())

os.chdir(home_directory)
print(os.getcwd())