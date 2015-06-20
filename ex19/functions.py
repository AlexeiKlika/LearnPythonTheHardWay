# define function and gives it two arguments
def cheese_and_crackers(cheese_count, boxes_of_creackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers" % boxes_of_creackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

# calls the function and includes explicit interegers
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "Or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# calls the functions and gives variables as parameters
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
# calls the functions and uses formula as parameter
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
# calls function with variables in formulas as parameters
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)