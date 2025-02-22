birim1 = input("Çevrilecek birim(kg/lbs): ")
kütle = float(input("Çevirilecek birimin miktarını yazınız: "))
pound = kütle * 2.205
kg = kütle * 0.453
if birim1 == "kg":
    print(f"{round(pound, 3)}lbs")
elif birim1 == "lbs":
    print(f"{round(kg, 3)}kg")
elif birim1 == "":
    print("Lütfen birim giriniz.")
else:
    print("Lütfen geçerli bir birim giriniz.")