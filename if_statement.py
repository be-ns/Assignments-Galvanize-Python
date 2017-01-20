import os
import time
import random

def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')


def do_the_math():
	clear()
	numm = input("number between 4 and 10 >")
	if numm > 7:
		numm += 3
		clear()
		print("We added three to your number {}".format(numm))
		print(numm)
		time.sleep(3)
		clear()
	elif numm < 7:
		numm += 10
		clear()
		print("We added 10 to the number you added in, {}.").format(numm)
		print(numm)
		time.sleep(3)
		clear()
	elif numm == 7:
		clear()
		print("It's Seven. Your number was Seven.")
		print(numm)
		time.sleep(3)
		clear()




def homework_one():
	clear()
	my_num = int(raw_input("number? > "))
	if my_num > 0:
		print("It's positive.")
	elif my_num < 0:
		print("It's negative.")
	else:
		print("It's zero.")


def homework_two():
	# Write a script that takes two user inputted numbers
	# and prints "The first number is larger" or
	#"The second number is larger" depending on which is larger.
	#(Hint: you'll need to use raw_input() twice.)
	clear()
	input_1 = int(raw_input("number choice 1 > "))
	input_2 = int(raw_input("number choice 2 > "))
	while input_1 and input_2:
		if input_1 > input_2:
			print("{} is larger than {}").format(input_1, input_2)
			break
		elif input_1 < input_2:
			print("{} is larger than {}").format(input_2, input_1)
			break
		else:
			print("They are equal. Dummy.")
			break


def homework_three():
	my_max = int(raw_input("Number here> "))
	my_sum = 0
	count = my_max
	while count > 0:
	     my_sum += count
	     count -= 1

	print(my_sum)


def homework_four():
	my_max = int(raw_input("Number here> "))
	my_sum = my_max
	count = my_max-1
	while count != 0:
	     my_sum *= count
	     count -= 1

	print(my_sum)


def homework_five():
	empty_list = []
	my_max = int(raw_input("Number here> "))
	for i in range(1, my_max):
		if my_max % i == 0:
			empty_list.append(i)

	print(empty_list)


def homework_six():
	empty_list = []
	my_max = int(raw_input("Number here> "))
	for i in range(1, my_max):
		if my_max % i == 0:
			empty_list.append(i)

	print(max(empty_list))


def homework_7():
	empty_list = []
	my_max = int(raw_input("Number here> "))
	for i in range(2, my_max):
		if my_max % i == 0:
			empty_list.append(i)

	print(min(empty_list))


def homework_8():
	empty_list = []
	my_max = int(raw_input("Number here> "))
	for i in range(1, my_max+1):
		if my_max % i == 0:
			empty_list.append(i)
			print(i)
	if empty_list[1] != my_max:
		print("{} is not a prime number").format(my_max)
	else:
		print("{} is a prime number").format(my_max)


def homework_9():
	bash = int(raw_input("Where should we start? >"))
	bash2 = bash
	exe = 1
	aye = 0
	while bash2 > 0:
		ans = ((2 * exe) + aye)
		bash2 -= 1
		aye = exe
		exe = ans
		continue

	print("the {}th element in the iteration would be {}").format(bash, ans)


def homework_ten():
	clear()
	value = int(raw_input("What number are we looking for? > "))
	truth = 1
	working = list(range(1, 7))
	while value:
		a = random.choice(working)
		b = random.choice(working)
		c = random.choice(working)
		d =	random.choice(working)
		e = random.choice(working)
		f = random.choice(working)
		if a != b and a != c and a != d and a != e and a != f:
			if b != c and b != d and b != e and b != f:
				if c != d and c != e and c != f:
					if d != e and d != f:
						if e != f:
							if (a + (b - c) * d - e) * f == value:
								print (a, b, c, d, e, f)
								break


# build a function in which you ask user what homework problem they wanna do.
# answer should be integer 1-10 inclusive
# select correct homework problem
# shows what the prompt was
# shows my code in quotes
# waits for 'n' input
# does math

# homework_one()
# homework_two()
# homework_three()
# homework_four()
# homework_five()
# homework_six()
# homework_7()
# homework_8()
# homework_9()
# homework_ten()
# do_the_math()
