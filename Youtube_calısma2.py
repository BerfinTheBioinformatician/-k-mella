#Nested loops: a loop within another looüü--
"""
outer loop:
    inner loop:"""
#for x in range(4): #dıştaki loop iç loopun 3 kere tekrarlanmasını sağlıyor.
 #   for y in range(1, 10): #değişken y diye başka bir harfle isimlendirildi
#      print(y, end="") #Yan yana sıralanmalarını sağladı
 #   print() #alt alta 3 sıra oluşturulmasını sağladı
"""
rows = int(input("Enter how many rows you desire: "))
columns = int(input("Enter how many columns you desire: "))
symbol = input("Enter how many symbol you desire: ")
for x in range(rows):
    for y in range (columns):
        print(symbol, end="")
    print()"""

#lists, sets, tuplets
#List = [] ordered and changeable, Duplicates OK
#Set = {} unordered and immutable, but Add/Remove OK, No duplicates
#Tuple () ordered and unchangeable, Duplicates OK. Faster
#List []
"""fruits = ["apple", "orange", "banana", "coconut"]"""

"""print(fruits[2])""" #The turnout is banana with this one
"""print(fruits[0:3])"""# from zero to 3
"""print(fruits[:3])"""#from zero to two
"""print(fruits[::2])"""#The ones on second step
"""print(fruits[::-1])"""#reversed

"""print(dir(fruits)) """#shows different kind of methods list can perform
"""
print(help(fruits))""" #shows what you can do with the list
"""print(len(fruits)) """#number of element

"""print("apple" in fruits)""" # is apple in the list question boolean

"""fruits[0] = "pinapple" """ # changes apple with pineapple
"""fruits.append("pineapple") """#adds pineapple to the list
"""fruits.remove("apple") """#removes the apple
"""fruits.insert("pineapple")"""# inserts the pineapple at the beginning
"""fruits.sort()"""#sorts the list in alphabetical order
"""fruits.reverse()"""#reversed 
"""fruits.clear()"""#clears the list
""""print(fruits.index("apple")) """#index of the object

#set {} (unorganized) can not use index #no duplicates
"""fruits.add("pineapple") """# adds
"""fruits.remove("apple")""" #removes
"""fruits.pop()""" #removes one element randomly

#Tuple () fast, unchangeable
"""fruits.index("apple")""" #index

#Shopping Cart Program
"""
foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy(q to quit): ")
    if food.lower() == "q":
        break
    else:
        foods.append(food)
        price = float(input(f"Enter the price of {food}: $"))
        prices.append(price)
print("-----Your Cart-----")
for food in foods:
    print(food, end=" ")
for price in prices:
    total += price
print()
print(f"Your total is: ${total}")"""

#shoppıng (Kendi denediğim)
"""
foods =[]
prices = []
total = 0

while True:
    food = input("Enter the food(q to quit): ")
    if food.lower() == "q":
        break
    else:
        foods.append(food)
        price = float(input("Enter the price: $"))
        prices.append(price)

print("----------Your Cart----------")

for food in foods:
    
    print(food, end=" ")

for price in prices:
    total += price
print()
print(f"Your total is ${total}.")"""

#2D collection
#2D list =[list1,list2,list3] (kinda like excel spreadsheet)
"""
fruits =     ["apple", "orange", "banana", "kiwi"]
vegetables = ["tomato", "cucumber", "celery"]
meats =      ["beef", "chicken", "lamb"]
groceries = [fruits, vegetables, meats]"""

"""print(groceries[0][0])""" #fruit listesindeki apple'ı gösterir, kordinat gibi

"""for collection in groceries:
    print(collection)""" #listleri alt alta sıraladı
"""
for collection in groceries:
    for food in collection:
        print(food, end=" ") #hepsini liste dışına çıkarıp yan yana sıraladı
    print()""" #liste içindeki itemleri yanyana aldı 
"""
num_pad = ((1, 2, 3), 
           (4, 5, 6,), 
           (7, 8, 9), 
           ("*", 0, "#"))
for row in num_pad:
    for num in row:
      print(num, end=" ")
    print()
""" #numpad printing

#Python quiz game
"""questions = ("How many finger humans have?: ",
            "What city is the capital of Turkiye?: ",
            "Which organel in human cell produce ATP?: ")
options = (("A. 2", "B. 5", "C. 10"), 
           ("A. Paris", "B. Ankara", "C. Beijing"), 
           ("A. Nukleus", "B. Ribosome", "C. Mitochondria"))

answers = ("C", "B", "C")
guesses = []  #list is used to append the guesses
score = 0
question_num = 0

for question in questions:
    print("--------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter your answer (A, B, C): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer.")"""

"""  question_num += 1""" #ilk for'un altında
#Her sorudan sonra kademe arttırarak diğer cevap şıkkının gelmesini sağlıyor.
"""
print("----------------------")
print("RESULTS")
print("----------------------")
print("Answers", end=" ")
for answer in answers:
    print(answer, end=" ")
print()
print("Guesses:", end=" ")
for guess in guesses:
    print(guess, end=" ")
score =int(score / len(questions)* 100)
print(f"Your score: {score} %")"""

#dictionaries= a collection of {key:value} pairs
#              ordered and cheangeable. No duplicates
"""capitals = {"USA": "Washington D.C.", 
           "India": "New Delhi",
            "China": "Beijing"}
print(capitals.get("China"))""" #capitali getiriyor.
"""capitals.update({"Germany": "Berlin"})""" #updates the set
"""capitals.popitem()""" #deletes the latest insert
"""capitals.clear()""" #cleans the dictionary
"""capitals.keys()""" #brings only the keys (kinda like a list)
"""capitals.values() """#brings only the values (kinda like a list)
"""capitals.items()""" #brings the items each one like a tuples (2d list)
#bulunmayan key'e None olarak cevap verir
#concession stand program
"""
items = {"Popcorn": 1.50,
         "Soda": 0.85,
         "Hot Dog": 2.00,
         "Water": 1.00}
cart = []
total = 0
print("----------MENU----------")
for key, value in items.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------------")

while True:
    food = input("Select an item (Q to quit): ").capitalize()
    if food == "Q":
        break
    elif items.get(food) is not None:
        cart.append(food)
print("--------YOUR CART--------")
for food in cart:
    total += items.get(food)
    print(food, end=" ")
print()
print(f"Your total is: ${total:.2f}.")"""

#Generating random numbers
import random
#print(help(random))
"""num = random.randint(1, 6)""" #selects one of random num
"""num = random.random() """# random floating num between 0-1

"""option = ("rock", "paper", "scissors")
option = random.choice(option)""" #great for games, select one of the given choices 

"""random.shuffle()""" #shuffles randomly
"""
lowest = 1    
highest = 50
answer = random.randint(lowest, highest)
guesses = 0
is_running = True
print("Python Number Guessing Game")
print(f"Select a number between {lowest}-{highest}")
while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses +=1
    else:
        print("Invalid guess.")
        print(f"Select a number between {lowest}-{highest}")

    if guess < lowest or guess > highest:
            print(f"This number is out off range please select a number between {lowest}-{highest}")
    elif guess < answer:
            print("Too low, try again!")
    elif guess > answer:
            print("Too high, try again!")
    else:
            print(f"CORRECT. The answer is {answer}.")
            print(f"Number of guesses {guesses}")
            is_running = False"""
#Taş kağıt makas
"""
options = ("rock", "paper", "scissors")
running = True
while running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player =input("Enter a choice(rock, paper, scissors): ").lower()

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
        print("You've lost!")
    if not input("Play again?(y/n): ").lower() == "y":
       running = False
        
print("Thanks for playing." )"""

"""
dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│ ●  ●  ● │",
        "│         │",
        "│ ●  ●  ● │",
        "└─────────┘")
}
dice = []
total = 0
num_of_dice = int(input("How many dice?: "))
for die in range(num_of_dice):
    dice.append(random.randint(1,6))"""
"""for line in range(5):
        for die in dice:
        print(dice_art.get(die)[line], end="")
    print() 
print()""" #yan yana sıralar
"""for die in dice:
    total += die
print(f"total: {total}")
"""
