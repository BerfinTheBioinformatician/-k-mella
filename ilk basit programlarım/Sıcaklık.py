b1 = input(
    "Dönüşmesini istediğiniz birim Celsius, Fahrenheit ve Kelvin arasından hangisidir?: "
    )

b2= input(
    "Dönüştürülmesini istediğiniz birim (Celsius, Fahrenheit, Kelvin): "
    )

d = float(input(
    "Girdiğiniz birim kaç derecedir?: "
    )) 
cf = (d * 9 / 5) + 32
ck = d + 273.15

fc = (d - 32) / 1.8
fk = (d + 459.6) * 5 / 9

kc = d - 273.15
kf = (d * 9 / 5) - 459.6

if b1 == "Celsius" and b2 == "Fahrenheit":
    print(round(cf, 2))
elif b1 == "Celsius" and b2 == "Kelvin":
    print(round(ck, 2))
elif b1 == "Fahrenheit" and b2 == "Celsius":
    print(round(fc, 2))
elif b1 == "Fahrenheit" and b2 == "Kelvin":
    print(round(fk, 2))
elif b1 == "Kelvin" and b2 == "Celsius":
    print(round(kc, 2))
elif b1 == "Kelvin" and b2 == "Fahrenheit":
    print(round(kf, 2))
else:
    print("Lütfen yalnızca sizden istenilen bilgileri girin.")

