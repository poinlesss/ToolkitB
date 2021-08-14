import glob

print('\nNamed with wildcard *:')
for name in glob.glob('/Users/me/Desktop/*'):
    print(name)
