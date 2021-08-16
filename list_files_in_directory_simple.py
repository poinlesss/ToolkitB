from os import listdir
from os.path import isfile, join

mypath = "/var/folders/lm/nzs5z0wd0910lx4wdjw6p3fw0000gn/T/S10.1/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print len((onlyfiles))
