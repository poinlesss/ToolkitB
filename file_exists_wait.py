import os.path
import sys
import time

arg1 = ""
n = len(sys.argv)
i = 0
time_to_wait = 30
emergency_abort = False
file_exists = False

for i in range(1, n):
    if i == 1:
        arg1 = sys.argv[i]
        file1 = arg1

if i == 0:
    print('No file defined, because no parameter passed.')
else:
    i = 0
    while not emergency_abort and not file_exists:
        if os.path.exists(arg1):
            folder_exists = True
        else:
            time.sleep(1)
        i = i + 1
        if i > time_to_wait:
            emergency_abort = True

    print('Folder exists: %s' % file_exists)
