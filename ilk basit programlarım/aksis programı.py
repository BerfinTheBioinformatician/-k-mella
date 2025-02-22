name = input("Kullanıcı adı: ")
giris = input("Tc kimlik no: ")
while not len(giris) == 11 or not giris.isdigit():
    print("Geçersiz kimlik numarası.")
    giris = input("Tc kimlik no: ")
sifre = input("Kullanıcı şifre: ")
vize = float(input("Vize notunuzu giriniz: "))
while vize < 0 or vize > 100:
    vize = float(input("Geçerli bir vize notu giriniz: "))
final = float(input("Final notunuzu giriniz: "))
while final < 0 or final > 100:
    final = float(input("Geçersiz final notu, lütfen notunuzu tekrar giriniz: "))
agno = (vize * 40 /100) + (final * 60 / 100)

if final < 50:
    print("Bu dersten kaldınız.")
elif agno >= 88:
    print("AA")
elif agno >= 80:
    print("BA")
elif agno >= 73:
    print("BB")
elif agno >= 66:
    print("CB")
elif agno >= 60:
    print("CC")
elif agno >= 55:
    print("DC")
elif agno >= 50:
    print("DD")
else:
    print("Bu dersten kaldınız.")

