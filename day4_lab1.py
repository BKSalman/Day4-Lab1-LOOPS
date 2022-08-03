for i in range(45, 210):
	if i == 100:
		continue
	elif i == 205:
		break
	else: 
		print(i)

x = input("What is the product of 7 * 24 ?\n")
while int(x) != 168:
	x = input("Your Answer is wrong try again..\n")

print("You answered this Question correctly")