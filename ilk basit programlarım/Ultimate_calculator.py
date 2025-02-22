print(
	"Welcome to The Calculator. Press Enter to continue."
)
s1 = input(
	"Sayı 1 : "
)
while not s1.isdigit():
		s1 = input(
			"Sayı 1 : "
)
s2 = input(
	"Sayı 2 : "
)
while not s2.isdigit():
	s2 = input(
	"Sayı 2 : "
)
islem = input(
	"Yapılacak işlem sembolünü giriniz(x,/,-,+): ".lower()
)

if islem == "x":
	a = int(s1) * int(s2)
	print(a)

elif islem == "/":
	b = int(s1) / int(s2)
	print(f"{b:.2f}")

elif islem == "+":
	c = int(s1) + int(s2)
	print(c)

elif islem == "-":
	d = int(s1) - int(s2)
	print(d)

else:
	print(f"Geçersiz sembol. {islem}")