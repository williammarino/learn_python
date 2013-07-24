print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	print "3. Pick up a knife and fight the bear"

	bear = raw_input("> ")

	if bear == "1":
		print "The bear eats your face off."
	elif bear == "2":
		print "The beat eats your legs off."
	elif bear == "3":
		print "You engage in melee combat with the bear."
		print "1. Stab the bear"
		print "2. Go for the bears throat."
		print "3. Run away the bear has overpowered you.  Why would you attack a bear?"

		attack = int(raw_input("> "))

		if attack == "1":
			print "You barely broke the skin.  RUN AWAY!"
		elif attack == "2":
			print "Success you were able to slit the throat of the bear and win the melee battle."
		elif attack == "3":
			print "Did you know bears can run up to 40 mph?  You were caught and eaten alive.  Nice try."
	else:
		print "Sorry, failure to follow directions has resulted in going insane." % bear

elif door == "2":
	print "you stare into the endless abyss at Cthulhu retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"

else:		
	print "You stumble around and fall on a knife and die. Good job!"