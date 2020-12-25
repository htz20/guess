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
		x = x - 1
		if guess > r :
			print("你的猜測比答案大喔")
		elif guess < r :
			print("你的猜測比答案小喔")
		if x == 0 :
			print ("答案是", r, "沒有機會了喔")
			break




