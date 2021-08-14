from os.path import expanduser
home_directory = expanduser("~")

import os, shutil;folder = home_directory + '/food';
for filename in os.listdir(folder):    file_path = os.path.join(folder, filename);
print('Failed to delete %s.' % (file_path));