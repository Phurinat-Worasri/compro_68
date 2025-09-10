filename = input('Enter filename: ')
try:
    infile = open(filename, 'r')
    content = infile.read()
    print(content)
    infile
except IOError:
    print('An error occurred trying to read the file.')
    print('the file',filename)
print('End of program')