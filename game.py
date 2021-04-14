import random 


def game ():
	
	ask = input("Do you wanna play a lil game ? y/n ").lower ()
	if ask == "y" or ask == "Y":
		print ("You need to find the right number between 10 and 50")
		print ("Be careful, you only have 3 chances to guess")
		state = 0
		x = random.randint (10,50)
		k = 1
		converted = str(x)
		converted = converted [:1]
		
			
		while True:
			
			y = int(input("What's your guess? "))
			state += 1
			
		
			if x == y:
				print ("Congrats")
				break
	
			if x != y:
				print ("No.. Try again")

			if state == 1:
				print ("Okay I'll give you a hint")
				if x % 2 == 0:
					print ("The hidden number is a multiple of 2")
				else:
					print ("The hidden number is not a multiple of 2")

			if state == 2:
				print ("Okay i see, I'll give you one last clue ")
				for i in range (len (converted)):
					print ("The first number of the hidden number is {}".format (converted))
		 
			
			if state == 3:
				print ("You didn't find, you have no more chance ")
				print ("The right answer to find was {}".format (x))
				break
			



		ask2 = input ("Do you wanna play again ? y/n ")
		if ask2 == "y" or ask2 == "Y":
			return (game ())
			

	elif ask != "y" or ask != "Y":
		print ("Okay maybe next time..")
		
	
		

game ()

