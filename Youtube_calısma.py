"""babe = "popo"
print(f"Hello {babe}") # f string ile yazım 


#VARIABLES
#Integers (tam sayı)

#Float (kesirli sayı)

price = 10.99
print(f"The price is {price} TL.")
agno = 2.96
print(f"My agno is {agno}.")


#Boolean (true or false)
is_student = True
print(f"Are you a student?: {is_student}")

for_sale = True
if for_sale:
    print("This item is on sale!")
else:
    print("This item is not on sale!")

lives_in_paris = False
if lives_in_paris:
    print("She lives in Paris.")
else:
    print("She does not live in Paris.")
    """
"""name = "Berfin"
age = 21
agno = 2.7
is_worker = False"""

"""name = bool(name)
print(name)"""

#input() {terminalde cevap verilebilir]
"""name = input("Enter your name: ")
city = input("Where do you live?: ")
print(f"Hello {name}!")
print(f"You live in {city}.")

age = input("How old were you last year?: ")
age = int(age)
age = 1 + age
print(f"Hello you will be {age} years old this year!") 
"""
"""name = input("Your name:" )
agno = float(input("What is your current agno?: "))
agno = agno + 5.6
print(f"Hello your new agno is {agno}.")"""

#Rectangle area calculator
"""lenght = float(input("Enter the rectangles lenght: "))
width = float(input("Enter the rectangles width: "))
area = lenght * width
print(f"Rectangles area is {area}cm².") #cm² için numlock + alt + 0178
print(area)
"""
#Shopping cart exercise
"""item = input("Which item do you require?: ")
item_price = float(input("What is the price?: "))
amount = int(input("How much are you gonna buy?: "))
tax = int(input("How much of tax it has?: %"))
total_cost = float((item_price * amount) + (item_price * amount * tax / 100))
print(f"You have bought {amount} x {item}/s!")
print(f"Your total cost is ${total_cost}.")
print("Thank you for choosing us!")"""

# Math Equations
"""friends = 0
friends += 1 #(friends2e olan yeni atama yani friends = friends + 1)
friends *= 5
friends /= 3
friends **= 2 #üs olarak atama
print(friends)"""
"""
x = 7.65
y = -2.15
result = round(x) # round en yakın tam sayıya yuvarlar.
result = abs(y) # abs sıfırdan uzaklık kademesi
result = pow(5, 3) # ikinci sayı ilk sayının üssü olarak konumlanır
result = max(x, y) # sonucların en büyüğünü seçer
result = min(x, y) #sonuçların en küçüğünü seçer
print(result)
"""
#import math /#bu komut ile matematiksel işlemler açılır (math.pi)
#print(math.pi) #import math ile math.pi/e/sqrt/sin(x) ve türevi değerleri direkt getirebiliriz
"""
x = 9.1
result = math.sqrt(x) 
result = math.sin(x)
print(result)
"""
#import math
"""
radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius # 2* pi* r
#print(f"The circumference is {circumference}")
print(f"The circumference is {round(circumference, 2)} cm") # virgülden sonra sadece iki basamağı gösterir
"""
#print(round(-math.log(25) * math.pi, 3)) #log ve pi arası işlemi yuvarladım, virgülden sonra 3 hane ekledım.

"""radius = float(input("Enter the radius of circle: "))
area = math.pi * pow(radius, 2)
print(f"The area of the circle is {round(area, 3)} cm²")"""

"""a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a, 2) + pow(b, 2)) #sqrt(square root yani karekök)
print(f"Side C equals to {c}.")"""

#if, elif, else
"""age = int(input("Enter your age: ")) #int sayısal karşılaştırmalar da kullanılmalı
if age < 0: # öncelikli istenmeyen durumlar en başa yazılmalı
    print("You have not been born yet.")
elif age < 18:
    print("You are not legally allowed to drive.")
elif age >100:
    print("You are too old to drive.")
else:
    print("You are legally allowed to drive.")
"""

"""response = input("Would you like some dessert (Yes/No): ")
if response == "Yes":
    print("Here is the dessert options: souffle, tiramisu, apple pie.")
elif response == "No":
    print("Here is the receipt.")
else:
    print("Please answer with only Yes or no.")
dessert = input("Which dessert would you like to order on the menu?: ")
amount = int(input("How many would you like to order?: ")) 
if dessert == "soufffle" or dessert == "tiramisu" or dessert == "apple pie":
    print(f"You have order {amount} x {dessert}, Thank you for choosing us! ")
else:
    print("We have no such thing on the menu.")"""
#boolean da if true'yu else de false'u temsil eder.

#logical operators = or, and, not
""" 
 or= at least  one condition must be true
and = both condition must be true
not = inverts the condition (not False, not True)"""

"""temp = int(input("What degree is outside?: "))
is_raining = False
if temp > 35 or temp < 0 or is_raining: #one of the condition to be true is enough to cancell
    print("The party is cancelled.")
else:
    print("The party is gonna be held according to the invitation!")"""

"""temp = int(input("What Celsius is the outside?: "))
is_sunny = True
if temp >= 20 and temp <= 35 and is_sunny:
    print("The party is gonna be held as usual.")
else:
    print("The party is cancelled")"""

#not kullanım örneği

"""temp = -9
is_sunny = True
if temp >= 20 and is_sunny:
    print("Its hot outside.")
    print("Its sunny.")
elif temp <= 0 and is_sunny:
    print("Its cold outside.")
    print("Its sunny.")    
elif 20 > temp > 0 and is_sunny:
    print("Its warm outside.")
    print("Its sunny.")
elif temp >= 20 and not is_sunny:
    print("Its hot outside.")
    print("Its cloudy.")
elif temp <= 0 and not is_sunny:
    print("Its cold outside.")
    print("Its cloudy.")    
elif 20 > temp > 0 and not is_sunny:
    print("Its warm outside.")
    print("Its cloudy.")
else: 
    print("We do not have the current data yet.")"""

#conditional statements : one line shortcut if else statement
"""x if "condition" else y (return x if the condition is true else return y)"""

"""num = 5"""
#print("Positive" if num > 0 else "Negative")
#result = "EVEN" if num % 2 == 0 else "ODD"

"""is_single = True
print("She is single" if is_single else "She is not single")"""

#string method
###len() (number of items in the container ex: name character )
"""name = input("Enter your name: ")"""
"""result = len(name)""" #lenght of name
"""result = name.find(" ")"""# finds first occurence of the desired object (starts with 0)
"""result = name.rfind("o")""" #finds Last occurence of the desired object) (if it cant find it gives -1 result)
"""name = name.capitalize()""" #Capitilizes the first letter
"""name = name.upper()""" # capitilizes all letters
"""name = name.lower()""" #all the characters lower case
"""result = name.isdigit()""" #checks if its all only digits or no
"""result = name.isalpha()""" #checks if its all letters (space " " too makes it false)
"""result = name.count("a")""" #counts how many desired objective it containts 
"""phone_number = input("Enter your phone number: +90 ")
phone_number = phone_number.replace("+90", "")"""
"""print(phone_number)"""

#print(help(str)) (Helps to see the string types)

#Example
"""use = input("Kullanıcı adı giriniz: ")"""
"""print("Kullanıcı adı kurallarla uyumlu." if use.isalpha() and len(use) <= 12 else "Geçerli bir ad giriniz.")""" # isalpha boşluk konulunca da false veriyor.
"""if len(use) >= 12:
    print("Kullanıcı adınız 12 karakteri geçmemelidir.")
elif not use.find(" ") == -1:
    print("Kullanıcı adınız boşluk içermemelidir.")
elif use.isalpha() == False:
    print("Kullanıcı adınız harf dışında bir obje içermemelidir.")
else:
    print(f"Hoşgeldin {use}")

"""
#indexing = accessing elements of a sequence using "[]" 
#                    [start : end : step] 

"""credit_number = "1576-7554-856-5656"""
"""print(credit_number[0])""" #ilk haneyi verdi
"""print(credit_number[0 : 4])""" #starting point inclusive ending po,nt exclusive so it stopped at "6"
"""print(credit_number[:4])""" #starting point automatically from beginning so 1576
"""credit_number[5:]""" # starts from 5 till the end
#negative index counts reversed (reverste 0 yerine 1. değer diyerek saymaya başlar)
#reverste negatif olduğu için ters yazılır 
#ör: credit_number[-4:] = 5656'yı önüne getirir
"""print(credit_number[::])""" #begining till the end
"""print(credit_number[::3])"""#0 ve üçün katlarında bulunan değerleri getirir.
#step kısmına -1 koymak veriyi tersine çevirip verir.

#format specifiers = {value:flags} format a value based on what flags are inserted.

"""price1 = 3.1415
price2 = -955.486
price3 = 12.76
price4 = 1565.54
price5 = -54.1
price6 = 56
price7 = 97.32
price8 = -2.37
price9 = 20456.65
price10 = 5681.76"""

"""print(f"Price 1 is ${price1:.2f}")""" #virgülden sonra hane getirmeye yarar, bu örnekte 2 basamak gösterirf = floating point number
"""print(f"Price 2 is ${price2:10}")""" #total 10 spaces to display the number
"""print(f"Price 3 is ${price3:010}")""" #total 10 spaces to display the number adds zero to the spaces in front
"""print(f"Price 4 is ${price4:<10}")"""#soldan başlayarak hizalanma, totalde 10 boşluk, boşluklara 0 ekler
"""print(f"Price 5 is ${price5:<10})"""# önde boşluklarla 10 haneli hizalama, öndeki boşluklara sıfır koymaz
"""print(f"Price 6 is ${price6:^10}")"""#sayılar ortalanacak şekilde hizalanır
"""print(f"Price 7 is ${price7:+}")"""# positive showed with "+" in front and negative displayed with "-"
"""print(f"Price 8 is ${price8: }")"""# evenly distrubuted negative and positive numbers
"""print(f"Price 9 is ${price9:,}")""" #bigger numbers such as thousand or million showed with coma
"""print(f"Price 10 is ${price10:+,.3f}")""" #flags can be combined 

#While loops
#executes some code while some condition remains true

"""name = input("Enter your name: ")
while name == "":
    print("You did not enter your name.")
    name = input("Enter your name: ")""" #repromted it or else the first print will become an infinite loop

"""print(f"Hello {name}")"""

"""color = input("Enter a color you like (q to quit): ")
while not color == "q":
    print(f"You like {color}")
    color = input("Enter another color you like (q to quit): ")
print("Bye.")
"""
#num = int(input("Enter a number between 1 - 10: "))
""" 
while num < 1 or num > 10:
    print(f"{num} is not between 1 - 10")
    num = int(input("Enter a number between 1 - 10: "))

print(f"Your number is {num}")
"""
#compound interest calculator exercise
"""principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero. ")

while rate <= 0:
    rate = float(input("Enter the rate: "))
    if rate <= 0:
        print("Rate can't be less than or equal to zero.")

while time <= 0:
    time = int(input("Enter the time as years: "))
    if time <= 0:
        print("The time cant be less or equal to zero.")

total = principle * pow((1 + rate / 100), time)
print(f"Your total balance after {time} year/s: ${total:^10.2f}")"""

#for loops = execute a block of code a ficed number of times
# You can itirate over a range, string, sequence
  
"""for x in range(1, 11):""" #in range firstd num inclusive second one exclusive
"""     print(x)"""
# reversed(range(1, 11)) counts from 10 to 1
#range(1, 11, 2) counts by 2 such as 1 3 5 7 9 
"""print("Happy new year!")"""
"""for x in range(1,21):
    if x == 13:"""
"""        continue """# continue 13'ü atlayarak devam etmesini sağladı
"""    else:
        print(x)"""

import time # Variables'ı mytime yaptm çünkü time yazınca hatalı oluyor.
"""
mytime = int(input("Süreyi saniye cinsinden giriniz: "))

for x in range(mytime, 0, -1):
    saniye = x % 60
    dakika = int(x / 60) % 60
    saat = int(x / 3600)
    print(f"{saat:02}:{dakika:02}:{saniye:02}")
    time.sleep(1)
"""
#counter