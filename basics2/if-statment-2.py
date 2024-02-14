num = int(input("enter a number: "))
if num >= 1500 and num <= 2700:
    if num % 7 == 0 and num % 5 == 0:
        print(f"{num} is divisible by 7 and 5")
    else:
        print(f"{num} is not divisible by 7 and 5")
else:
    print("invalid number")