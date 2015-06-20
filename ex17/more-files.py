from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could these two on one line, how?
# maybe this -> indata = open(from_file).read()
in_file = open(from_file)
indata = in_file.read()

# print "The input file is %d bytes long" % len(indata)

if exists(to_file):
	print "'%s' already exists" % to_file
	print "To overwrite, hit RETURN or CTRL-C to abort."
	raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

out_file.close()
in_file.close()

print "Copy complete"