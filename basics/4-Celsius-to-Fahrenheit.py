kind = input("what you want to convert, celsius or fahrenheit: ")
num = int(input("enter the temperature: "))
if kind == "celsius":
    print("the temperature in fahrenheit is: ", ((num * 1.8) + 32))
else:
    print("the temperature in celsius is: ", ((num - 32) / 1.8))
