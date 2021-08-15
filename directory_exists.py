import os.path
#from os.path import expanduser
import sys

n = len(sys.argv)
i = 0

for i in range(1, n):
    if i == 1:
        arg1 = sys.argv[i]
        folder = arg1

if i == 0:
    print('No directory defined, because no parameter passed.')
else:
    print(os.path.exists(arg1))  # True