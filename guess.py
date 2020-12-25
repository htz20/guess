import random
r = random.randint(1, 100)
x = 3

while True:
	guess = input("來猜猜看: ")
	guess = int(guess)
	if guess == r :
		print ("u get the correct ans!")
		break
	else:
		x = x-1
		print ("try again")
		if x == 0:
			print ("答案是:", r, "喔")
			break


