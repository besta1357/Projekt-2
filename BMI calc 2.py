vyska = float(input("vyska v metrech: "))
vaha = float(input("vaha v kilogramech: "))
jmeno = input("zadej svoje jmeno: ")
bmi = round((vaha / vyska**2), 2)
print("Jméno: " + str(jmeno) + " - " + "BMI: " + str(bmi))
if bmi < 18.5:
    print("Podváha")
elif 18.5 <= bmi < 25:
    print("Normální váha")
elif 25 <= bmi < 30:
    print("Nadváha")
elif 30 <= bmi < 35:
    print("Obezita 1. stupně")
elif 35 <= bmi < 40:
    print("Obezita 2. stupně")
elif bmi >= 40:
    print("Obezita 3. stupně")
else:
    print("Neznámá hodnota")
print("Konec programu")
print("Děkujeme za použití BMI kalkulačky")
print("Konec programu")