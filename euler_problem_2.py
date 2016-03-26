# Even Fibonacci numbers
# Problem 2
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

oldTerm1 = 1
oldTerm2 = 2
sumVal = 0
# print oldTerm1
while (oldTerm2 <= 4000000):
	if (oldTerm2 % 2 == 0):
		# print oldTerm2
		sumVal += oldTerm2
		# print "sum of values: %d" % sumVal
	tempVal = oldTerm2
	oldTerm2 = oldTerm2 + oldTerm1
	oldTerm1 = tempVal


print sumVal