import random
r = random.randint(1, 100)
x = 0

while True:
	x = x + 1
	guess = input("來猜猜看: ")
	guess = int(guess)
	
	if guess == r :
		print ("u get the correct ans!")
		break
	else:
		if guess > r :
			print("你的猜測比答案大喔")
		elif guess < r :
			print("你的猜測比答案小喔")
		print ("你猜了", x, "次")





