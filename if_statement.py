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
    print("Write a script that takes a user inputted number and prints whether it is positive, negative or zero.")
    print("\n")
    time.sleep(4)
    my_num = int(raw_input("number? > "))
    if my_num > 0:
        print("It's positive.")
    elif my_num < 0:
        print("It's negative.")
    else:
        print("It's zero.")


def homework_two():
	clear()
	print("Write a script that takes two user inputted numbers and prints which is larger.")
	time.sleep(4)
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
	clear()
	print("Write a script that computes the sum of all numbers from 0 to a user inputted number.")
	print("This time though, start at the user inputted number and work down.")
	print("This answer will look very much like the example above, you'll just need to change a couple of things.")
	time.sleep(5)
	clear()
	my_max = int(raw_input("Number here> "))
	my_sum = 0
	count = my_max
	while count > 0:
		 my_sum += count
		 count -= 1

	print(my_sum)


def homework_four():
	clear()
	print("Write a script that computes the factorial of a user inputted number.")
	time.sleep(5)
	clear()
	my_max = int(raw_input("Number here> "))
	my_sum = my_max
	count = my_max-1
	while count != 0:
		 my_sum *= count
		 count -= 1

	print(my_sum)


def homework_five():
	clear()
	print("Write a script that computes and prints all of the divisors of a user inputted number.")
	time.sleep(5)
	clear()
	empty_list = []
	my_max = int(raw_input("Number here> "))
	for i in range(1, my_max):
		if my_max % i == 0:
			empty_list.append(i)

	print(empty_list)


def homework_six():
	clear()
	print("Write a script that computes the greatest common divisor between two user inputted numbers.")
	time.sleep(5)
	clear()
	this_list = []
	my_min = int(raw_input("Smaller Number here> "))
	my_max = int(raw_input("Larger, Second number here> "))
	boogie = list(range(my_min, my_max + 1))
	for ints in boogie:
		if my_max % ints == 0 and my_min % ints == 0:
			this_list.append(ints)
		else:
			pass
	if this_list:
		print(max(this_list))
	else:
		print("There are no common divisors in that range.")


def homework_7():
	# smallest positive integer that is divisible by both a and b.
	clear()
	print("Write a script that computes the LCM between two user inputted numbers.")
	time.sleep(5)
	clear()
	empty_list = []
	my_min = int(raw_input("Small-ish Number here> "))
	my_max = int(raw_input("Large-ish Number here> "))
	for ints in range(my_max, my_max*my_min):
		if ints % my_max == 0 and ints % my_min == 0:
			empty_list.append(ints)
		else:
			pass
	if empty_list:
		print(min(empty_list))
	else:
		print("There is no LCM for these values.")


def homework_8():
	clear()
	print("Write a script that determines whether or not a user inputted number is a prime number.")
	time.sleep(3)
	clear()
	empty_list = []
	my_max = int(raw_input("Number here> "))
	difference = (my_max-1) - 2
	xyz = 0
	for i in range(2, my_max-1):
		if my_max % i == 0:
			print("{} is not a prime number").format(my_max)
			break
		else:
			xyz += 1
	if xyz == difference:
		print("{} is a prime number.").format(my_max)


def homework_9():
	clear()
	print("Write a script that prints the Nth element in the series as determined by input from the user.")
	print("e.g. If the user inputs the number 3, the script should print the 3rd element in the series")
	print("The series is: Z = ((2 * X) + Y)")
	print("where X starts at 1, and Y starts at 0")
	print("After each iteration, Y resets to X. X resets to Z from previous stage.")
	time.sleep(8)
	clear()
	bash = int(raw_input("What number in the series do you want to see? >"))
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
	print("Challenge: solve the equation:")
	print("(a + (b - c) * d - e) * f = [user input]")
	print("Options include 22, 38, 46, 57, 78, 80, 81, 88, 92, 100, 102, 104, 105")
	value = int(raw_input("What number are we looking for? > "))
	truth = 1
	working = list(range(1, 7))
	count = 100000
	while count > 0:
		a = random.choice(working)
		b = random.choice(working)
		c = random.choice(working)
		d =	random.choice(working)
		e = random.choice(working)
		f = random.choice(working)
		count -= 1
		if a != b and a != c and a != d and a != e and a != f:
			if b != c and b != d and b != e and b != f:
				if c != d and c != e and c != f:
					if d != e and d != f:
						if e != f:
							if (a + (b - c) * d - e) * f == value:
								print (a, b, c, d, e, f)
								break
	if count == 0:
		print("No values solve the equation.")

def choose_problem():
	homeworks = [1, 2, 3, 4, 5, 6 ,7 , 8, 9, 10]
	user_input = int(raw_input("Which homework problem should we look at?> "))
	if user_input in homeworks:
		if user_input == 1:
			homework_one()
		if user_input == 2:
			homework_two()
		if user_input == 3:
			homework_three()
		if user_input == 4:
			homework_four()
		if user_input == 5:
			homework_five()
		if user_input == 6:
			homework_six()
		if user_input == 7:
			homework_7()
		if user_input == 8:
			homework_8()
		if user_input == 9:
			homework_9()
		if user_input == 10:
			homework_ten()
		if user_input == 0:
			do_the_math()
	else:
		clear()
		print("That's not one of the options. 0 - 10 only.")
		time.sleep(3)
		clear()
		choose_problem()

choose_problem()

# shows what the prompt was
# shows my code in quotes
# waits for 'n' input
# does math
