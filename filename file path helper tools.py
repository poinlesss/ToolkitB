import os.path
import functools
import contextlib
import textwrap

pathname = "/Users/K/dir/subdir/k.py"

os.path.split(pathname)
# what it does
# ('/Users/K/dir/subdir', 'k.py')

(dirname, filename) = os.path.split(pathname)

print('dirname: ' + dirname)
print('pathname: ' + pathname)


print('filename: ' + filename)
(shortname, extension) = os.path.splitext(filename)
print('shortname: ' + shortname)
print('extension: ' + extension)

