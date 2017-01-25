import os
import time

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def factorial():
    clear()
    print("Write a script that computes and prints the factorial of a user inputted number.")
    time.sleep(4.5)
    what_you_say = int(raw_input("Pick a number> "))
    print what_you_say ** what_you_say


def is_prime():
    clear()
    print("Write a script that determines if a user inputted number is prime.")
    time.sleep(5)
    my_max = int(raw_input("Number here> "))
    difference, xyz = (my_max - 2), 0
    for i in range(2, my_max):
        if my_max % i == 0:
            print('{} is not a prime number').format(my_max)
            break
        else:
            xyz += 1
    if xyz == difference:
        print("{} is a prime number.").format(my_max)


def two_one():
    clear()
    print("Write a script that obtains the count of a user inputted letter in a user inputted string")
    x = (raw_input("type any word> ")).lower()
    y = int(raw_input("Which number in that sequence should we look at?> ")) - 1
    b = x.count(x[y])
    z = list('abcdefghijklmnopqrstuvwxyz')
    a = (x[y])
    for idx, letts in enumerate(z):
        if letts == a:
            clear()
            print("The letter '{0}' appears {1} times in {2} and is the {3} letter in the alphabet").format(x[y], b, x, z[idx])


def exclamatory():
    clear()
    print("Write a script that prints a user iputted string in all caps if it ends in '!'")
    time.sleep(3)
    what = raw_input("enter any string, with or without a '!' > ")
    if what[-1] == '!':
        print(what).upper()
    else:
        print("Boring-sauce - doesn't end in a '!'")


def remove_vowels():
    clear()
    print("Write a script that removes all vowels from the inputted string")
    time.sleep(4)
    word = raw_input("what string should we remove vowels from? > ")
    vowels = list('aeiou')
    for char in word:
        if char in vowels:
            word = word.replace(char, '_')
    clear()
    print(word)


def cap_every_other():
    clear()
    print("Write a script that makes every other letter capitalized")
    time.sleep(2.75)
    string = raw_input("pick any word > ")
    for idx, char in enumerate(string):
        if idx % 2 == 0 or idx == 0:
            string = string.replace(char, char.upper(), 1)

    clear()
    print(string)


def even_only():
    clear()
    print("Write a script that creates a list of only even numbers between 0 and user inputted number.")
    time.sleep(3)
    even_and_odd = raw_input("give us a large number> ")
    full_list = range(2, (int(even_and_odd) - 1), 2)
    clear()
    print(full_list)


def divisors_only():
    clear()
    print("Write a script that creates a list of all divisors from 0 to a user inputted number")
    time.sleep(2.5)
    inputted = list(range(1, (int(raw_input(" Assign the number to the top of the range in which we will look > ")) + 1))) # this gets the top end of range
    divisor = int(raw_input("This is the number we want to divide by > "))
    output = []# 'divisor' this gets the divisible number
    for num in inputted:
        if num % divisor == 0:
            output.append(num)
    clear()
    print(output)


def common_elements():
    clear()
    print("Two lists of numbers are made through user inputs. A new list is made with all common elements.")
    time.sleep(3)
    number_1 = int(raw_input(" Number larger than 20 here: "))
    number_2 = int(raw_input(" number less than 5 here: "))
    number_3 = int(raw_input(" Different, Number more than 20 here: "))
    number_4 = int(raw_input(" different number less than 5 here: "))

    list_1, list_2, empty_list = list(range(number_2, number_1, number_2)), list(range(number_4, number_3, number_4)), []
    for num in list_1:
        if num in list_2:
            empty_list.append(num)
    print(empty_list)


def multiples_of_x():
    clear()
    print("Write a script that outputs all multiples of 'x' between 0 and 'y'.")
    print("both are user inputs")
    time.sleep(2.75)
    numbah = int(raw_input("Give us a large number (this is y)> "))
    numbah_2 = int(raw_input('Give us a smaller number (this is x)> '))
    gonna_print = list(range(numbah_2, numbah + 1, numbah_2))
    clear()
    print(gonna_print)


def get_question():
    clear()
    print("Options for Problems to see are: ")
    options = ['m', 'c', 'd', 'e', 'a', 'f', 'p', 'u', 'l', 'r']
    print("[M]ultiples, [C]ommon Elements, [D]ivisors, [E]vens only, [A]lphabet numbers, [F]actorials, ")
    print("[P]rime number finder, [U]ppercase every other letter, [L]ook for '!', [R]emove all vowels. ")
    question = raw_input("What problem should we look at? ").lower().strip()
    if question in options:
        if question == 'm':
            multiples_of_x()
        if question == 'c':
            common_elements()
        if question == 'd':
            divisors_only()
        if question == 'e':
            even_only()
        if question == 'a':
            two_one()
        if question == 'f':
            factorial()
        if question == 'p':
            is_prime()
        if question == 'u':
            cap_every_other()
        if question == 'l':
            exclamatory()
        if question == 'r':
            remove_vowels()
    else:
        clear()
        print("That isn't an option.")
        get_question()

get_question()
