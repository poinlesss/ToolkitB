import glob
from os.path import expanduser
home_directory = expanduser("~")

print('\nNamed with wildcard *:')
for name in glob.glob(home_directory + '/Desktop/*'):
    print(name)
