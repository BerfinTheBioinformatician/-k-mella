ad = input("Adınız: ")
soyad = input("Soyadınız: ")
yas = int(input("Yaşınız: "))
print("MERHABA " + ad + " " + soyad)
if yas >= 65:
    print("ÇOK YAŞLISINIZ!!!!")
elif yas > 40 and yas < 65:
    print("YASLISIN MEZAR BAKMAYA BASLA.")
elif yas > 27:
    print("İŞ EV COCUK, KISACA YETİŞKİN.")
elif yas > 17:
    print("ÇITIRRRRRRRRR GENÇ.")
elif yas > 12:
    print("Ergenuss.")
elif yas > 5:
    print("aptal çocuk.")
elif yas >= 0:
    print("agu bugu bebe.") 
else:
    print("Dalga geçme p1ç >:( ")