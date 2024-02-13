kind = input("what you want to convert, C or F: ")
num = int(input("enter the temperature: "))
if kind == "C":
    print("the temperature in fahrenheit is: ", ((num * 1.8) + 32))
elif kind == "F":
    print("the temperature in celsius is: ", ((num - 32) / 1.8))
else:
    print("invalid choice")