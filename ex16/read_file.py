from sys import argv

script, user_file = argv

txt = open(user_file)
print txt.read()
print "Have a nice day! Bye now!"