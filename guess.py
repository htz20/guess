import random
start = input ("選擇你開始的範圍：")
end = input ("選擇你結速的範圍：")
start = int(start)
end = int(end)

r = random.randint(start, end)
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





