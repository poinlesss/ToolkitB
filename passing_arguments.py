# watching for files to exist
# accepting multiple parameters
# send in file path with file names
# python

import sys
import os, shutil

n = len(sys.argv)

arg1 = ''
arg2 = ''
arg3 = ''
arg4 = ''
arg5 = ''
arg6 = ''
arg7 = ''
arg8 = ''
arg9 = ''
arg10 = ''


for i in range(1, n):

    if i == 1:
        arg1 = sys.argv[i]
    if i == 2:
        arg2 = sys.argv[i]
    if i == 3:
        arg3 = sys.argv[i]
    if i == 4:
        arg4 = sys.argv[i]
    if i == 5:
        arg5 = sys.argv[i]
    if i == 6:
        arg6 = sys.argv[i]
    if i == 7:
        arg7 = sys.argv[i]
    if i == 8:
        arg8 = sys.argv[i]
    if i == 9:
        arg9 = sys.argv[i]
    if i == 10:
        arg10 = sys.argv[i]


print(arg1)
print(arg2)
print(arg3)
print(arg4)
print(arg5)
print(arg6)
print(arg7)
print(arg8)
print(arg9)
print(arg10)
