def plus(x, y):
    return x+y


def minus(x, y):
    return x-y


def multiply(x, y):
    return x*y


def divided(x, y):
    return x/y


print("1 - add")
print("2 - subtract")
print("3 - multiply")
print("4 - divided")

choice = int(input("Choose your operation (1/2/3/4): "))
if choice in [1, 2, 3, 4]:
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))
    if choice == 1:
        result = num1+num2
    elif choice == 2:
        result = num1-num2
    elif choice == 3:
        result = num1*num2
    elif choice == 4:
        result = num1/num2
    print(f"The result of the operation is {result}")
else:
    print("invalid syntax number")
