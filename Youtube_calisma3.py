#functions = A block of reusable code
#			place () after the funcction name to invoke it

"""def information():""" #Helped to get all the statements into information() as a whole
"""	print("I am 56 years old.")
	print("I love playing guitar.")
	print("I like kayaking.")
	print("I am a US citizen.")
	print()

information() """

"""def information(name, age): #position of the parameters matter
	print(f"{name} is {age} years old.")
	print("I love playing guitar.")
	print("I like kayaking.")
	print("I am a US citizen.")
	print()"""

"""information("Laila", 25)""" #adding arguments
"""information("Bailey", 34)"""
"""information("Lolo", 96) """#added multiple arguments that differs from each other

#return = statement used to end a function
#			and send a result back to the caller

"""def add(x, y):
	z = x + y
	return z""" #returns the addition of x and y
"""def create_name(first, last):""" #returns the arguments written
"""	first = first.capitalize()
	last = last.capitalize()
	return first + " " + last
full_name = create_name("lloyd", "smith")
print(full_name)
"""
#default arguments = A default value for certain parameters
#					default is used when that argument is omitted(atlanmış)
#					make your functipn more flexible, educes # of arguments

"""def net_price(list_price, discount=0, tax=0.05): """#Deafulted the discount and tax
"""	return 	list_price * (1 - discount) * (1 + tax)		"""
"""print(net_price(500, 0.1, 0)) """#can change the default with addition
"""
import time
def count(end, start=0):
	for x in range(start, end+1):
		print(x)
		time.sleep(1)
	print("DONE!")
count(10)""" #starts from 0 to 10
# keyword arguments = an argument preceded by an identiifier
#					helps with readibility
#					order of arguments doesnt matter
"""
def hello(greeting, title, first, last):
	print(f"{greeting} {title} {first} {last}.")

hello("Hello", title="Mr.", first="Lloyd", last="Smith")"""
#with keywords placements doesnt matter anymore
#but still the positional arguments used first so gotta be front of the keywords
"""
def get_phone(country, area, first, last):
	return f"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=1, area=123, first=123, last=1234)
print(phone_num)
"""
# *args = allows you to pass multiple non-key arguments
#**kwargs = allows you to pass multiple keyword arguments
#			* unpacking operator

"""def add(*args):""" #args could be changed to num or else, "*" is more important
"""		total = 0
		for arg in args:
			total += arg
		return total
	print(add(1, 2, 3, 4))"""
"""
def display_name(*args):
	for arg in args:
		print(arg, end=" ")
display_name("Spongebob", "Squarepants")"""

"""def print_address(**kwargs):""" #used as a dictionary
"""	for key, value in kwargs.items():
		print(f"{key}: {value}")

print_address(street="123 Bakery St.", 
			  city="Detroit", 
			  state="Michigan")"""
"""
def shipping_label(*args, **kwargs):
	for arg in args:
		print(arg, end=" ")
	print()
	print(f"{kwargs.get('street')}")
	print(f"{kwargs.get('city')} {kwargs.get('state')} ")

shipping_label("Dr.", "Spongebob", "Squarepants", street="123 Fake St.", city="Detroit", state="Michigan")"""

#Iterables = An object\collection that can return its elements one at a time.
#			allowing it to be iterated over in a loop
"""
numbers = [1, 2, 3, 4, 5]

for number in reversed(numbers): #reversable
	print(number)"""
"""
fruits = {"apple", "orange", "banana", "coconut"}
for fruit in fruits:
	print(fruit)"""
#sets are not reversable bcuz it always change
"""
name = "BERFİN"
for characters in name:
	print(characters, end=" ") """#Harf harf ayırdı
"""
my_dictionary ={"A": 1, "B": 2, "C": 3}
for key in my_dictionary:
	print(key)"""
#only brings key till we write my_dictionary.values()

#Membership operators = used to test whether a value or variable is found in a sequance
# 						(string, list, tuple, set or dictionary)
#						1.in
#						2. not in
"""
word = "apple"
letter = input("Guess a letter in the secret word: ").lower()

if letter in word:
	print(f"There is a/an {letter}.")
else:
	print(f"{letter} was not found.")"""
"""
students = {"Spongebob", "Patric", "Sandy"}
student = input("Enter the name of a student: ").capitalize()

if student not in students:
	print(f"{student} is not in the list.")
else:
	print(f"{student} is in the list.")"""
"""
grades = {"Sandy": "A", 
		  "Spongebob": "B", 
		  "Squidward": "B"}
student = input("Enter the name of the student: ").capitalize()

if student in grades.keys():
	print(f"{student}'s grade is {grades.get(student)}")
else:
	print(f"{student} is not in the list.")
"""
#list comprehensions = a concise way to create lists in Python
#						Compact and easier to read than traditional loops
#						[expression for value in iterable if condition]
"""
doubles = []
for x in range(1, 11):
	doubles.append(x * 2)
print(doubles)""" #traditional
"""
doubles = {y * 2 for x in range(1, 11)}
print(doubles)""" #list comprehensions
"""
squares = [z * z for x in range(1, 11)]
print(squares)"""
"""
fruits = ["apple", "banana", "kiwi"]
fruits =[fruit[0] for fruit in fruits]
print(fruits)""" #returns first latter of the fruits
"""
numbers = [1, -2, -6, 5, 8, -11]
positive_num = [num for num in numbers if num >= 0]
print(positive_num)""" #returns positive numbers

