rain=input("Is it raining? (yes/no)")
temp=int(input("What is the temperature(in degree Celsius)?"))
if rain=="yes":
    if temp<=10:
        print("Wear a heavy rain jacket and boots!")
    elif temp>10:
        print("Bring an umbrella and a light raincoat.")
elif rain=="no":
    if temp<=15:
        print("It's chilly! Wear a warm sweater or jacket.")
    elif temp>15 and temp<25:
        print("Perfect weather! A t-shirt or light shirt is fine.")
    elif temp>=25:
        print("It's hot outside! Wear shorts and stay hydrated.")
else:
    print("invalid weather input")