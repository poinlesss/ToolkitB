#wait for files to exist

import os.path
import sys
import time

n = len(sys.argv)
i = 0
arg1 = ""; arg2 = ""; arg3 = ""; arg4 = ""; arg5 = ""; arg6 = ""; arg7 = ""; arg8 = ""; arg9 = ""; arg10 = "";
file1 = ""; file2 = ""; file3 = ""; file4 = ""; file5 = ""; file6 = ""; file7 = ""; file8 = ""; file9 = ""; file10 = "";
time_to_wait = 30
emergency_abort = False
files_exist = False

for i in range(1, n):
    if i == 1:        arg1 = sys.argv[i];         file1 = arg1
    if i == 2:        arg2 = sys.argv[i];         file2 = arg2
    if i == 3:        arg3 = sys.argv[i];         file3 = arg3
    if i == 4:        arg4 = sys.argv[i];         file4 = arg4
    if i == 5:        arg5 = sys.argv[i];         file5 = arg5
    if i == 6:        arg6 = sys.argv[i];         file6 = arg6
    if i == 7:        arg7 = sys.argv[i];         file7 = arg7
    if i == 8:        arg8 = sys.argv[i];         file8 = arg8
    if i == 9:        arg9 = sys.argv[i];         file9 = arg9
    if i == 10:        arg10 = sys.argv[i];         file10 = arg10

if i == 0:
    print('No file defined, because no parameter passed.')
else:
    i = 0
    while not emergency_abort and not files_exist:
        if file1 and os.path.exists(arg1):            file1 = ""
        if file2 and os.path.exists(arg2):            file2 = ""
        if file3 and os.path.exists(arg3):            file3 = ""
        if file4 and os.path.exists(arg4):            file4 = ""
        if file5 and os.path.exists(arg5):            file5 = ""
        if file6 and os.path.exists(arg6):            file6 = ""
        if file7 and os.path.exists(arg7):            file7 = ""
        if file8 and os.path.exists(arg8):            file8 = ""
        if file9 and os.path.exists(arg9):            file9 = ""
        if file10 and os.path.exists(arg10):            file10 = ""

        if file1 or file2 or file3 or file4 or file5 or file6 or file7 or file8 or file9 or file10:
            time.sleep(1)
            i = i + 1
        else:
            files_exist = True
        if i > time_to_wait:
            emergency_abort = True

    print('Files exist: %s' % files_exist)
