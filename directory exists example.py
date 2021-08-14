import os.path
from os.path import expanduser
home_directory = expanduser("~")

print(os.path.exists(home_directory)) #True
print(os.path.isfile(home_directory + "/Desktopa")) #True
print(os.getcwd())
print(os.getgroups())
print(os.getlogin())
print(os.getuid())
print(os.uname())
