#print "How old are you?",
#age = raw_input()
#print "How tall are you?",
#height = raw_input()
#print "How much do you weight?",
#weight = raw_input()

#print "So, your %r old, %r tall and %r heavy." % (
#	age, height, weight)



print ('-' * 30)
print ('Main Menu')
print ('-' * 30)
print ('1.Backup oracle database')
print ('2.Erase all data from database')
print ('3.You are just an idiot')
print ('-' * 30)


print ("Please select from the above menu 1-3"),
i = raw_input()

i = int(i)

if i == 1:
	print "Performing backup", "-" * 30