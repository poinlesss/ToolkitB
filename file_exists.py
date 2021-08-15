import os.path
import sys

arg1 = ""
n = len(sys.argv)
i = 0

for i in range(1, n):
    if i == 1:
        arg1 = sys.argv[i]
        file1 = arg1

if i == 0:
    print('No file defined, because no parameter passed.')
else:
    file_exists = os.path.exists(arg1)
    print(file_exists)  # True