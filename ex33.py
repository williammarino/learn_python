import sys

#i = 0
#numbers = []

#while i < 6:
#	print "At the top i is %d" % i
#	numbers.append(i)
#
#	i += 1
#	print "Numbers now:", numbers
#	print "At the bottom i is %d" % i

#print "The Numbers: "
#
#for num in numbers:
#	print num


def number_range(maxn, step):
	f = 0 
	numbers = []

	while f < maxn:
		print "At the top f is %d" % f
		numbers.append(f)

		f += step
		print "Numbers are now:", numbers
		print "At the bottom f is %d" % f

def number_range_using_for(max, step):
	#elements = range(0, max, step)
	for item in elements:
		print "Item: %d" % item
	print elements

#number_range(10,2)
number_range_using_for(24,2)


if __name__ == "__main__":
 	print sys.argv