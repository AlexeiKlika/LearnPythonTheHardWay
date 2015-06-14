# imports the argument values from the 'sys' module
from sys import argv

# unpacks the argument values by assignment each to variables
script, filename = argv

# opens the file specified by the 'filename' argument and saves the file object to the variable 'txt'
txt = open(filename)

# prints the file's name
print "Here's your file %r:" % filename
# reads the txt file objects and then prints it
print txt.read()
# close file
txt.close()

### promts the enter a file name that will be read
# print "Type the filename again:"
### user inputs file name
# file_again = raw_input("> ")

### user selected file will be opened as file object
#txt_again = open(file_again)

### file object assigned to 'txt_again' will  be read and printed to screen
#print txt_again.read()
### close file
# txt_again.close()