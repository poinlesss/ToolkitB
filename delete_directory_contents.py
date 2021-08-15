#expects one parameter (the target folder)

import sys
import os, shutil
from os.path import expanduser

home_directory = expanduser("~")

n = len(sys.argv)

arg1 = ''
i = 0

for i in range(1, n):
    if i == 1:
        arg1 = sys.argv[i]
        folder = arg1

if i == 0:
    print('No directory defined, because no parameter passed.')
else:
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
