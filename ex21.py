def add(a,b):
	print "Adding %d + %d" % (a, b)
	return a + b
	
def subtract(a, b):
	print "Subtracting %d - %d" % (a, b) 
	return a - b
	
def multiply(a, b):
	print "Multiply %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print "dividing %d / %d" % (a, b)
	return a / b
	
print "lets do some math with just functions!"

age = add(30, 5)
age = add(2, 1)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age,height, weight, iq)



print "This is a test"