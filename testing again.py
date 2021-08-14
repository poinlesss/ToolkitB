import os, shutil;folder = '/Users/me/food';
for filename in os.listdir(folder):    file_path = os.path.join(folder, filename);
print('Failed to delete %s.' % (file_path));