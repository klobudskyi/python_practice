# 1 (00:00:00) python tutorial for beginners 🐍
"""
print("I like Big Tasty!")
print("It's really good!")
"""

# from functools import total_ordering

# 2 (00:05:49) variables ❎
# A containers for a value (string, integer, float, boolean)
# A variable behaves as if it was the value it contains

# Strings
# first_name = "Dmytro"
# food = "Big Tasty"
# email = "dmytro.klobudskyi@gmail.com"

# Integers
# age = 23
# quantity = 3
# num_students = 30

# Float
# price = 10.99
# gpa = 3.2
# distance = 5.5

# Boolean
# is_student = True
# for_sale = False
# is_online = True

# To use formatted string literals, begin a string with f or F before the opening quotation mark or triple
# quotation mark. Inside this string, you can write a Python expression between { and } characters that can refer
# to variables or literal values.

"""
print(f"Hello {first_name}")
print(f"You like {food}?")
print(f"Your email is {email}")
print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_students} students")
print(f"The price is ${price}")
print(f"Your GPA is {gpa}")
print(f"You ran {distance} km")
print(f"Are you a student?: {is_student}")
"""

"""
if is_student:
    print("You are a student!")
else:
    print("You are not a student!")

if for_sale:
    print("That item is for sale!")
else:
    print("That item is not for sale!")

if is_online:
    print("You are online!")
else:
    print("You are offline!")
"""

# 3 (00:16:05) type casting 💱
# The process of converting a variable from one data type to another
# str(), int(), float(), bool()
"""
print(type(first_name))
print(type(age))
print(type(gpa))
print(type(is_student))

first_name = bool(first_name)
gpa = int(gpa)
age = float(age)
is_student = str(is_student)

print("->")

print(type(first_name))
print(type(age))
print(type(gpa))
print(type(is_student))
"""
# 4 (00:21:15) user input ⌨️
# input() - a function that prompts the user to enter data
# Returns the entered data as a string

"""
name = input("What is your name?: ")
age = int(input("How old are you?: "))

age = age + 1

print(f"Hello {name}!")
print("Happy Birthday!")
print(f"You are {age} years old!")
"""

# Rectangle Area Calculation
"""
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width

print(f"The area is: {area} cm^2")
"""

# Shopping Cart Program
"""
item = str(input("What item would you like to buy?: "))
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${total}")
"""

# 5 (00:32:42) ⭐ madlibs game 📖
# Word game where you create a story by filling in blanks with random words
"""
adjective_1 = input("Enter and adjective (description): ")
noun_1 = input("Enter a noun (person, place, thing): ")
adjective_2 = input("Enter and adjective (description): ")
verb_1 = input("Enter a verb ending with '-ing': ")
adjective_3 = input("Enter and adjective (description): ")

print(f"Today I went to a {adjective_1} zoo")
print(f"In an exhibit, I saw a {noun_1}")
print(f"{noun_1} was {adjective_2} and {verb_1}")
print(f"I was {adjective_3}!")
"""

# 6 (00:37:55) arithmetic & math 📐

# friends = 10

# Addition
# friends = friends + 1
# friends += 1

# Subtraction
# friends = friends - 2
# friends -= 2

# Multiplication
# friends = friends*3
# friends *= 3

# Division
# friends = friends / 2
# friends /= 2

# Exponentiation
# friends = friends ** 2
# friends **= 2

# Modulus
# remainder = friends % 2

# print(remainder)

# Built-in math related functions

# x = 3.14
# y = -4
# z = 5

# result = round(x)
# result = abs(y)
# result = pow(z, 2)
# result = max(x, y, z)
# result = min(x, y, z)

# print(result)

# Constants and functions

# import math

# print(math.pi)
# print(math.e)

# result = math.sqrt(z)
# result = math.ceil(x)
# result = math.floor(x)

# print(result)

# Calculate the circumference of the circle

# import math

# radius = float(input("Enter the radius of the circle: "))

# circumference = 2 * math.pi * radius

# print(f"The circumference is: {round(circumference, 2)} cm")

# Calculate the area of the circle

# import math

# radius = float(input("Enter the radius of the circle: "))

# area = math.pi * pow(radius, 2)

# print(f"The area of the circle is: {round(area, 2)} cm^2")

# Find the hypotenuse of the right triangle

# import math

# a = float(input("Enter side A: "))
# b = float(input("Enter side B: "))

# c = math.sqrt(pow(a, 2) + pow(b, 2))

# print(f"Side C = {c}")

# 7 (00:51:46) if statements 🤔
# Do some code only IF some condition is True
# Else do something else
"""
age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up!")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You must be 18+ to sign up!")
"""

# Food example
"""
response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")
"""

# Name example
"""
name = input("Enter your name: ")

if name == "":
    print("You did not type your name!")
else:
    print(f"Hello {name}!")
"""

# Boolean example
"""
for_sale = True

if for_sale:
    print("This item is for sale!")
else:
    print("This item is not for sale!")

online = False

if online:
    print("The user is online!")
else:
    print("This user is offline!")
"""

# 8 (01:00:06) ⭐ calculator program 🧮
"""
operator = input("Enter the operator (+ - * /): ")
num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

if operator == "+":
    result = num_1 + num_2
    print(round(result, 2))
elif operator == "-":
    result = num_1 - num_2
    print(round(result, 2))
elif operator == "*":
    result = num_1 * num_2
    print(round(result, 2))
elif operator == "/":
    result = num_1 / num_2
    print(round(result, 2))
else:
    print(f"{operator} is not a valid operator!")
"""

# 9 (01:05:59) ⭐ weight conversion program 🏋️
"""
weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight *= 2.205
    unit = "lbs"
    print(f"Your weight is: {round(weight, 2)} {unit}")
elif unit == "L":
    weight /= 2.205
    unit = "kgs"
    print(f"Your weight is: {round(weight, 2)} {unit}")
else:
    print(f"{unit} is not valid!")
"""
# 10 (01:09:59) ⭐ temperature conversion program 🌡️
"""
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")#
temperature = float(input("Enter the temperature: "))

if unit == "C":
    temperature = round((9 * temperature) / 5 + 32, 2)
    print(f"The temperature in Fahrenheit is: {temperature} °F")
elif unit == "F":
    temperature = round((temperature - 32) * 5 / 9, 2)
    print(f"The temperature in Celsius is: {temperature} °C")
else:
    print(f"{unit} is an invalid unit of measurement!")
"""

# 11 (01:13:58) logical operators 🌦️
# Evaluate multiple conditions (or, and ,not)
# or = at least one condition must be True
# and = both conditions must be True
# not = inverts the condition (not False, not True)

# or
"""
temperature = 25
is_raining = False

if temperature > 35 or temperature < 0 or is_raining:
    print("The outdoor event is cancelled!")
else:
    print("The outdoor event is still scheduled!")
"""

# and + not
"""
temperature = 20
is_sunny = False

if temperature >= 30 and is_sunny:
    print("It is hot outside 🥵")
    print("It is sunny ☀️")
elif temperature <= 0 and is_sunny:
    print("It is cold outside 🥶")
    print("It is sunny ☀️")
elif 30 >= temperature >= 20 and is_sunny:
    print("It is warm outside 😌")
    print("It is sunny ☀️")
elif temperature >= 30 and not is_sunny:
    print("It is hot outside 🥵")
    print("It is cloudy ☁️")
elif temperature <= 0 and not is_sunny:
    print("It is cold outside 🥶")
    print("It is cloudy ☁️")
elif 30 >= temperature >= 20 and not is_sunny:
    print("It is warm outside 😌")
    print("It is cloudy ☁️")
"""
# 12 (01:21:28) conditional expressions ❓
# A one-line shortcut for the if-else statement (ternary operator)
# Print or assign one of two values based on a condition
# X if condition else Y
"""
num = 5
a = 6
b = 7
age = 13
temperature = 30
user_role = ("guest")
# print("Positive" if num > 0 else "Negative")
# print("Even" if num % 2 == 0 else "Odd")
# max_num = a if a > b else b
# min_num = a if a < b else b
# status = "Adult" if age >= 18 else "Child"
# weather = "Hot" if temperature > 20 else "Cold"
access_level = "Full access" if user_role == "admin" else "Limited access"
print(access_level)
"""

# 13 (01:27:03) string methods 〰️

# name = input("Enter your full name: ")
# phone_number = input("Enter your phone_number: ")

# result = len(name)
# result = name.find(" ")
# result = name.rfind(" ")
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = phone_number.count("-")
# phone_number  = phone_number.replace("-", " ")
# print(phone_number)

# print(help(str))

# Validate user input
# - username is no more than 12 characters
# - username must not contain spaces
# - username must not contain digits

"""
username = input("Enter your username: ")

if len(username) > 12:
    print("Your username can't be more than 12 characters!")
elif username.find(" ") != -1:
    print("Your username can't contain spaces!")
elif username.isdigit():
    print("Your username can't contain numbers!")
else:
    print(f"Welcome {username}!")
"""

# 14 (01:39:08) string indexing ✂️
# Accessing elements of a sequence using [] (indexing operator)
# [start : end : stop]

# credit_number = "1234-5678-9012-3456"

# print(credit_number[0])
# print(credit_number[:4])
# print(credit_number[5:9])
# print(credit_number[5:])
# print(credit_number[-4])
# print(credit_number[::3])
# last_digits = credit_number[-4:]
# credit_number = credit_number[::-1]
# print(f"XXXX-XXXX-XXXX-{last_digits}")
# print(credit_number)

# 15 (01:46:35) format specifiers 💬
# {value:flags} format a value based on what flags are inserted
# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator
"""
price_1 = 3.14159
price_2 = -987.65
price_3 = 1200.34

print(f"Price 1 is ${price_1:.2f}")
print(f"Price 2 is ${price_2:>10}")
print(f"Price 3 is ${price_3:+,}")
"""

# 16 (01:51:55) while loops ♾️
# While loop - execute some code WHILE some condition remains true
"""
name = input("Enter your name: ")

while name == "":
    print("You did not enter your name!")
    name = input("Enter your name: ")
    
print(f"Hello {name}!")
"""

"""
age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative!")
    age = int(input("Enter your age: "))

print(f"You are {age} years old!")
"""

"""
food = input("Enter a food you like (q to quit): ")

while food != "q":
    print(f"You like {food}!")
    food = input("Enter another food you like (q to quit): ")

print("Bye!")
"""

"""
num = int(input("Enter a number between 1 to 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 to 10: "))

print(f"Your number is {num}!")
"""

# 17 (01:58:53) ⭐ compound interest calculator 💵
"""
principal = 0
rate = 0
time = 0

while True:
    principal = float(input("Enter the principal amount: "))
    if principal < 0:
        print("Principal can't be less than zero!")
    else:
        break
while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than zero!")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be less than zero!")
    else:
        break

total = principal * pow((1 + rate / 100), time)

print(f"Balance after {time} year/s: ${total:.2f}")
"""

# 18 (02:06:28) for loops 🔁
# For loops execute a block of code a fixed number of times.
# You can iterate over a range, string, sequence, etc.
"""
for x in reversed(range(1, 11)):
    print(x)

print("Happy New Year!")
"""

"""
credit_card = "1234-5678-9012-3456"

for x in credit_card:
    print(x)

print("Happy New Year!")
"""

"""
for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)
"""

# 19 (02:11:33) ⭐ countdown timer program ⌛
"""
import time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's up!")
"""

# 20 (02:17:28) nested loops ➿
# A loop within another loop (outer, inner)
# outer loop:
#       inner loop:
"""
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")
    print()
"""

# 21 (02:23:03) lists, sets, and tuples 🍎
# Collection = single "variable" used to store multiple values

# List  = [] ordered and changeable, duplicates OK
# fruits = ["apple", "orange", "banana", "coconut"]

# for fruit in fruits:
#    print(fruit)

# print(fruits[::-1])
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# fruits[0] = "pineapple"
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("coconut"))
# print(fruits.count("banana"))

# Set   = {} unordered and immutable, but Add/Remove OK, NO duplicates
# fruits = {"apple", "orange", "banana", "coconut"}

# Tuple = () ordered and unchangeable, duplicates OK, faster
# fruits = ("apple", "orange", "banana", "coconut")

# 22 (02:38:08) ⭐ shopping cart program 🛒
"""
foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")

print()

for food in foods:
    print(food)

for price in prices:
    total += price

print()

print(f"Your total is: ${total}")
"""

# 23 (02:45:21) 2D collections ⬜
"""
fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

print(groceries[0][0])
"""

"""
groceries = [["apple", "orange", "banana", "coconut"],
             ["celery", "carrots", "potatoes"],
             ["chicken", "fish", "turkey"]]

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
"""

"""
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()
"""

# 24 (02:53:59) ⭐ quiz game 💯

"""
questions = (
    "How many elements are in the periodic table?: ",
    "Which animal lays the largest eggs?: ",
    "What is the most abundant gas in Earth's atmosphere?: ",
    "How many bones are in the human body?: ",
    "Which planet in the solar system is the hottest?: ",
)

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale ", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter A, B, C or D: ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer!")

    question_num += 1

print(" ")
print("Results: ")
print(" ")

print("- answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("- guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = (score / len(questions) * 100)
print()
print(f"Your score is: {score}%")
"""

# 25 (03:03:27) dictionaries 📙
# Dictionary - a collection of {key:value} pairs ordered and changeable. No duplicates.

"""
capitals = {"USA":"Washington D.C.",
            "India":"New Delhi",
            "China":"Beijing",
            "Ukraine":"Kyiv"}
"""

# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("Ukraine"))

# if capitals.get("Ukraine"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")

# capitals.update({"Germany":"Berlin"})
# capitals.update({"USA":"Moscow"})

# capitals.pop("China")
# capitals.popitem()

# capitals.clear()

# keys = capitals.keys()
# for key in keys:
#    print(key)

# values = capitals.values()
# for value in values:
#    print(value)

# items = capitals.items()
# for key, value in items:
#     print(f"{key}: {value}")

# 26 (03:11:33) ⭐ concession stand program 🍿

"""
menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

cart = []
total = 0

print("------ MENU ------")

for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

print("------------------")

while True:
        food = input("Select an item (Q to quit): ").lower()
        if food == "q":
                break
        elif menu.get(food) is not None:
                cart.append(food)

print("------ ORDER ------")

for food in cart:
        total += menu.get(food)
        print(food, end=" ")

print()
print("------ TOTAL ------")
print (f"Total is: ${total:.2f}")
"""

# 27 (03:19:42) random numbers 🎲

"""
import random

low = 1
high = 100

options = ("rock","paper","scissors")
cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

# number = random.randint(low, high)
# number = random.random()
# option = random.choice(options)
# random.shuffle(cards)

print(cards)
"""

# 28 (03:24:16) ⭐ number guessing game 🔢

"""
import random

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num, highest_num)

guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}:")

while is_running:

        guess = input("Enter your guess: ")

        if guess.isdigit():
                guess = int(guess)
                guesses += 1

                if guess < lowest_num or guess > highest_num:
                        print("That number is out of range")
                        print(f"Please select a number between {lowest_num} and {highest_num}:")
                elif guess < answer:
                        print("Too low! Try again!")
                elif guess > answer:
                        print("Too high! Try again!")
                else:
                        print(f"CORRECT! The answer was {answer}")
                        print(f"Number of guesses: {guesses}")
                        is_running = False
        else:
                print("Invalid guess!")
                print(f"Please select a number between {lowest_num} and {highest_num}:")
"""

# 29 (03:32:37) ⭐ rock, paper, scissors game 🗿

"""
import random

options = ("rock","paper","scissors")

running = True

while running:

        player = None
        computer = random.choice(options)

        while player not in options:
                player = input("Enter a choice (rock, paper, scissors): ")

        print(f"Player: {player}")
        print(f"Computer: {computer}")

        if player == computer:
                print("It's a tie!")
        elif player == "rock" and computer == "scissors":
                print("You win!")
        elif player == "paper" and computer == "rock":
                print("You win!")
        elif player == "scissors" and computer == "paper":
                print("You win!")
        else:
                print("You lose!")

        if not input("Play again? (y/n): ").lower() == "y":
                running = False

print("Thanks for playing!")
"""

# 30 (03:42:06) ⭐ dice roller program ⚂

# import random
#
# dice_art = {
#     1: ("┌─────────┐",
#         "│         │",
#         "│    ●    │",
#         "│         │",
#         "└─────────┘"),
#     2: ("┌─────────┐",
#         "│  ●      │",
#         "│         │",
#         "│      ●  │",
#         "└─────────┘"),
#     3: ("┌─────────┐",
#         "│  ●      │",
#         "│    ●    │",
#         "│      ●  │",
#         "└─────────┘"),
#     4: ("┌─────────┐",
#         "│  ●   ●  │",
#         "│         │",
#         "│  ●   ●  │",
#         "└─────────┘"),
#     5: ("┌─────────┐",
#         "│  ●   ●  │",
#         "│    ●    │",
#         "│  ●   ●  │",
#         "└─────────┘"),
#     6: ("┌─────────┐",
#         "│  ●   ●  │",
#         "│  ●   ●  │",
#         "│  ●   ●  │",
#         "└─────────┘"),
# }
#
# dice = []
# total = 0
# num_of_dice = int(input("How many dice?: "))
#
# for die in range(num_of_dice):
#     dice.append(random.randint(1, 6))
#
# # for die in range(num_of_dice):
# #     for line in dice_art.get(dice[die]):
# #         print(line)
#
# for line in range(5):
#     for die in dice:
#         print(dice_art.get(die)[line], end="")
#     print()
#
# for die in dice:
#     total += die
# print(f"Total: {total}")

# 31 (03:52:12) functions 📞

# function = A block of reusable code
#            place () after the function name to invoke it

# def happy_birthday(name, age):
#     print(f"Happy birthday to {name}!")
#     print(f"You are {age} years old!")
#     print("Happy birthday to you!")
#     print()
#
# happy_birthday("Bro", 20)
# happy_birthday("Steve", 30)
# happy_birthday("Joe", 40)

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}!")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")
#
# display_invoice("Dmytro", 42.50, "01/01")

# return = statement used to end a function
#          and send a result back to the caller

# def add(x, y):
#     z = x + y
#     return z
#
# def subtract(x, y):
#     z = x - y
#     return z
#
# def multiply(x, y):
#     z = x * y
#     return z
#
# def divide(x, y):
#     z = x / y
#     return z
#
# print(add(1, 2))
# print(subtract(1, 2))
# print(multiply(1, 2))
# print(divide(1, 2))

# def create_name(first, last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last
#
# full_name = create_name("dmytro", "klobudskyi")
#
# print(full_name)

# 32 (04:02:50) default arguments 👍

# - A default value for certain parameters
# - Default is used when that argument is omitted
# - Make your functions more flexible, reduces # of arguments
# - positional, default, keyword, arbitrary

# def net_price (list_price, discount = 0, tax = 0.05):
#     return list_price * (1 - discount) * (1 + tax)

# print(net_price(500))

# print(net_price(500, 0.1, 0))

# import time
#
# def count(end, start = 0):
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print("Done!")
#
# count(30, 15)

# 33 (04:08:56) keyword arguments 🗝️

# - An argument preceded by an identifier
# - Helps with readability
# - Order of arguments doesn't matter

# def hello(greeting, title, first, last):
#     print(f"{greeting} {title}{first} {last}")
#
# hello("Hello","Mr.","Dmytro","Klobudskyi") # positional arguments
#
# hello(title = "Mr.", first = "Dmytro", greeting = "Hello", last = "Klobudskyi") # keyword arguments

# for x in range(1, 10):
#     print(x, end = " ")

# print("1","2","3","4","5", sep = "-")

# def get_phone(country, area, first, last):
#     return f"{country}-{area}-{first}-{last}"
#
# phone_num = get_phone(country = "+380-99", area = "332", first = "48", last = "66")
#
# print(phone_num)

# 34 (04:15:40) *args & **kwargs 📦 # arbitrary arguments

# *args = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword arguments

# * = unpacking operator

# def add(a, b):
#     return a + b
#
# print(add(1 ,2))

# def add(*args):
#     print(type(args)) # <class 'tuple'>
#
# add(1 ,2)

# def add(*args):
#     total = 0
#     for arg in args :
#         total += arg
#     return total
#
# print(add(1, 2, 3, 4))

# def display_name(*args):
#     for arg in args:
#         print(arg, end = " ")
#
# display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")

# def print_address(**kwargs):
# print(type(kwargs)) # <class 'dict'>

# for value in kwargs.values():
#     print(value)

# for key in kwargs.keys():
#     print(key)

# for key, value in kwargs.items():
#     print(f"{key}: {value}")

# print_address(house = "17",
#               street = "Beregova St.",
#               village = "Yuriivka",
#               district = "Voznesensk",
#               area = "Mykolaiv",
#               zip = "55444")

# def shipping_label(*args, **kwargs):
#     for arg in args:
#         print(arg, end = " ")
#     print()
#
#     if "apt" in kwargs:
#         print(f"{kwargs.get("street")} {kwargs.get("apt")}")
#     elif "pobox" in kwargs:
#         print(f"{kwargs.get("street")}")
#         print(f"{kwargs.get("pobox")}")
#     else:
#         print(f"{kwargs.get("street")}")
#     print(f"{kwargs.get("city")} {kwargs.get("state")} {kwargs.get("zip")}")
#
# shipping_label("Dr.", "Spongebob", "Squarepants",
#                street = "Fake St.",
#                pobox = "PO box #1001",
#                city = "Detroit",
#                state = "MI",
#                zip = "54321")

# 35 (04:30:33) iterables 🔂

# An object/collection that can return its elements one at a time, allowing it to be iterated over in a loop

# numbers = (1, 2, 3, 4, 5) # or list
#
# for number in reversed(numbers):
#     print(number)


# fruits = {"apple", "orange", "banana", "coconut"}
#
# for fruit in fruits:
#     print(fruit)

# name = "Dmytro"
#
# for character in name:
#     print(character, end = " ")

# my_dictionary = {"A": 1, "B": 2, "C": 3}
#
# for key, value in my_dictionary.items():
#     print(f"{key} = {value}")

# 36 (04:37:04) membership operators 🔎

# Used to test whether a value or variable is found in a sequence (string, list, tuple, set or dictionary):
# - in
# - not in

# word = "APPLE"
#
# letter = input("Guess a letter in rhe secret word: ")
#
# if letter in word:
#     print(f"There is a {letter}")
# else:
#     print(f"{letter} was not found")
#
# if letter not in word:
#     print(f"{letter} was not found")
# else:
#     print(f"There is a {letter}")

# students = {"Spongebob", "Patrick", "Sandy"}
#
# student = input("Enter the name of a student: ")
#
# if student in students:
#     print(f"{student} is a student")
# else:
#     print(f"{student} was not found")
#
# if student not in students:
#     print(f"{student} was not found")
# else:
#     print(f"{student} is a student")

# grades = {"Sandy": "A",
#           "Squidward": "B",
#           "Spongebob": "C",
#           "Patrick": "D"}
#
# student = input("Enter the name of a student: ")
#
# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} was not found")

# email = "dmytro.klobudskyi@gmail.com"
#
# if "@" in email and "." in email:
#     print("Valid email")
# else:
#     print("Invalid email")

# 37 (04:45:56) list comprehensions 📃

# List comprehension = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

# doubles = []
#
# for x in range (1, 11):
#     doubles.append(x * 2)
#
# print(doubles)

# ↓

# doubles = [x * 2 for x in range(1, 11)]
#
# print(doubles)

# triples = [y * 3 for y in range(1, 11)]
# squares = [z * z for z in range(1, 11)]

# fruits = ["apple", "orange", "banana", "coconut"]
#
# fruit_chars = [fruit[0] for fruit in fruits]
# print(fruit_chars)

# numbers = [1, -2, 3, -4, 5, -6, 7, -8]
# positive_nums = [num for num in numbers if num >= 0]
# negative_nums = [num for num in numbers if num <= 0]
# even_nums = [num for num in numbers if num % 2 == 0]
# odd_nums = [num for num in numbers if num % 2 == 1]
#
# print(odd_nums)

# grades = [85, 42, 79, 90, 56, 61, 30]
# passing_grades = [grade for grade in grades if grade >= 60]
#
# print(passing_grades)

# 38 (04:56:17) match-case statements 📆

# Match-case statement (switch): An alternative to using 'elif' statements
#                                Execure some code if a value matches a 'case'
#                                Benefits: cleaner and syntax is more readable

# def day_of_week(day):
#     if day == 1:
#         return "It is Sunday"
#     elif day == 2:
#         return "It is Monday"
#     elif day == 3:
#         return "It is Tuesday"
#     elif day == 4:
#         return "It is Wednesday"
#     elif day == 5:
#         return "It is Thursday"
#     elif day == 6:
#         return "It is Friday"
#     elif day == 7:
#         return "It is Saturday"
#     else:
#         return "Not a valid day"
#
# print(day_of_week(1))

# ↓

# def day_of_week(day):
#     match day:
#         case 1:
#             return "It is Sunday"
#         case 2:
#             return "It is Monday"
#         case 3:
#             return "It is Tuesday"
#         case 4:
#             return "It is Wednesday"
#         case 5:
#             return "It is Thursday"
#         case 6:
#             return "It is Friday"
#         case 7:
#             return "It is Saturday"
#         case _:
#             return "Not a valid day"
#
# print(day_of_week(1))

# def is_weekend(day):
#     match day:
#         case "Saturday" | "Sunday":
#             return True
#         case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday" | _ :
#             return False
#
# print(is_weekend("Friday"))

# 39 (05:02:13) modules 📨

# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in on your own)
#          useful to break up a large program reusable separate files

# print(help("modules"))

# import math as m
# from math import pi

# import example
#
# result = example.pi
# result = example.square(3)
# result = example.cube(3)
# result = example.circumference(3)
# result = example.area(3)
#
# print(result)

# 40 (05:08:51) scope resolution 🔬

# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

"""
def func1():
    a = 1 # local scope
    print(a)

def func2():
    b = 2 # local scope
    print(b)
"""

"""
def func1():
    b = 2

    def func2():
        print(b) # enclosed scope

    func2()

func1()
"""

"""
def func1():
    print(x)

def func2():
    print(x)

x = 3 # global scope

func1()
func2()
"""

"""
from math import e

print(e) # built-in scope
"""

# 41 (05:14:22) if name == 'main': 📥

# if name == main: this script can be imported or run standalone

# Functions and classes in this module can be reused without the main block of code executing

# Example: library (import library for functionality, when running library directly - display a help page)

# Good practice: code is modular, helps readability, leaves no global variables, avoid unintended execution

# def main():
#     print("Hello, World!") # program

# if __name__ == '__main__':
#     main()

# 42 (05:23:34) ⭐ banking program 💰

# def show_balance(balance):
#     print("********************")
#     print(f"Your balance is ${balance:.2f}")

# def deposit():

#     print("********************")
#     amount = float(input("Enter an amount to be deposited: "))

#     if amount < 0:
#         print("********************")
#         print("That's not a valid amount")
#         return 0
#     else:
#         return amount

# def withdraw(balance):

#     print("********************")
#     amount = float(input("Enter an amount to be withdrawn: "))

#     if amount > balance:
#         print("********************")
#         print("Insufficient funds")
#         return 0
#     elif amount < 0:
#         print("********************")
#         print("Amount must be greater than 0")
#         return 0
#     else:
#         return amount
# def main():     # при запуску цього файлу в іншому файлі - нам не потрібно відображати цю частину коду,
#     balance = 0 # тому ми використовуємо "if __name__ == '__main__'", тобто ця функція буде виконуватись лише при запуску напряму
#     is_running = True

#     while is_running:
#         print("********************")
#         print("Banking program:")
#         print("********************")
#         print("1. Show Balance")
#         print("2. Deposit")
#         print("3. Withdraw")
#         print("4. Exit")
#         print("********************")

#         choice = input("Enter your choice (1-4): ")

#         if choice == '1':
#             show_balance(balance)
#         elif choice == '2':
#             balance += deposit()
#         elif choice == '3':
#             balance -= withdraw(balance)
#         elif choice == '4':
#             is_running = False
#         else:
#             print("********************")
#             print("That is not a valid choice")

#     print("********************")
#     print("Thank you! Have a nice day!")

# if __name__ == '__main__': # дослівне пояснення - "Якщо ми запускаємо файл напряму: виконай цей код"
#     main()

# 43 (05:38:34) ⭐ slot machine 🎰

# import random

# def spin_row():
#     symbols = ['🍒','🍉','🍋','🔔','⭐']

#     # results = []
#     # for symbol in range(3):
#     #     results.append(random.choice(symbols))
#     # return results

#     return [random.choice(symbols) for _ in range(3) ]


# def print_row(row):
#     print("-------------")
#     print(" │ ".join(row))
#     print("-------------")

# def get_payout(row, bet):
#     if row[0] == row[1] == row[2]:
#         if row[0] == '🍒':
#             return bet * 2
#         elif row[0] == '🔔':
#             return bet * 3
#         elif row[0] == '🍉':
#             return bet * 4
#         elif row[0] == '⭐':
#             return bet * 5
#         elif row[0] == '🍋':
#             return bet * 6
#     return 0

# def main():
#     balance = 100

#     print("-----------------------")
#     print("Welcome to Python Slots")
#     print("-----------------------")
#     print("Symbols:🍒🍉🍋🔔⭐")

#     while balance > 0:
#         print("-----------------------")
#         print(f"Current balance: ${balance}")

#         bet = input("Place your bet amount: ")

#         if not bet.isdigit():
#             print("Please enter a valid number")
#             continue

#         bet = int(bet)

#         if bet > balance:
#             print("Insufficient funds")
#             continue

#         if bet <= 0:
#             print("Bet must be greater than 0")
#             continue

#         balance -= bet

#         row = spin_row()
#         print("Spinning ...")
#         print_row(row)

#         payout = get_payout(row, bet)

#         if payout > 0:
#             print(f"You won ${payout}")
#         else:
#             print("Sorry, you lost this round")

#         balance += payout

#         play_again = input("Do you want to spin again? (Y/N):").upper()

#         if play_again != 'Y':
#             break
#     print("--------------------------------------------")
#     print(f"Game over! Your final balance is ${balance}")
#     print("--------------------------------------------")

# if __name__ == '__main__':
#     main()

# 44 (05:58:45) ⭐ encryption program 🔐
# 45 (06:07:26) ⭐ hangman game 🕺
# 46 (06:32:32) python object oriented programming 🚗
# 47 (06:44:50) class variables 🎓
# 48 (06:53:06) inheritance 👨‍👦‍👦
# 49 (07:00:02) multiple inheritance 🐟
# 50 (07:08:04) super() 🔴
# 51 (07:21:10) polymorphism 🎭
# 52 (07:29:15) duck typing 🦆
# 53 (07:33:34) static methods ⚡
# 54 (07:39:31) class methods 🏫
# 55 (07:46:16) magic methods 🌟
# 56 (07:59:51) @property ⚙️
# 57 (08:07:33) decorators 🎊
# 58 (08:14:57) exception handling 🚦
# 59 (08:20:46) file detection 🕵️‍♂️
# 60 (08:27:47) writing files ✍
# 61 (08:41:33) reading files 🔍
# 62 (08:48:29) dates & times 📅
# 63 (08:54:46) ⭐ alarm clock ⏰
# 64 (09:05:03) multithreading 🧵
# 65 (09:13:45) request API data ↩️
# 66 (09:22:19) PyQt5 GUI intro 🖥️
# 67 (09:31:27) PyQt5 labels 🏷️
# 68 (09:40:23) PyQt5 images 📷
# 69 (09:46:28) PyQt5 layout managers 🧲
# 70 (09:53:07) PyQt5 buttons 🛎️
# 71 (10:00:12) PyQt5 checkboxes ✅
# 72 (10:06:42) PyQt5 radio buttons 🔘
# 73 (10:15:55) PyQt5 line edits 💬
# 74 (10:21:55) PyQt5 CSS styles 🎨
# 75 (10:32:48) ⭐ digital clock program 🕒
# 76 (10:48:38) ⭐ stopwatch program ⏱
# 77 (11:06:05) ⭐ weather API app ☀️
