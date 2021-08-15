#expects a parameter

import os.path
import sys



def write_to_clipboard(output):
    import subprocess
    process = subprocess.Popen('pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode())


if __name__ == '__main__':
    arg1 = ""
    n = len(sys.argv)
    i = 0

    for i in range(1, n):
        if i == 1:
            arg1 = sys.argv[i]
            write_to_clipboard(arg1)

    if i == 0:
        print('No parameter passed.')
