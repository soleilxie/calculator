def Add(a, b):
    return (a + b)

def Sub(a, b):
    return (a - b)

def Mul(a, b):
    return (a * b)

def Div(a, b):
    return (a / b)

def Exp(a, b):
    result = 1
    if b == 0:
        return 1
    while b > 0:
        result = result*a
        b -= 1
    return result

def Fac(a):
    result = a
    i = 1
    if a == 0 or a == 1:
        return 1
    else:
        while i < a:
            result = i*result
            i += 1
        return result 
choice = 0
while choice != 7:
    print()
    print("1. Add 2 Numbers")
    print("2. Subtract 2 Numbers")
    print("3. Multiply 2 Numbers")
    print("4. Divide 2 Numbers")
    print("5. Exponent of 1 Number")
    print("6. Factorial of 1 Number")
    print("7. Exit")
    print()
    
    choice = int(input("Your Choice: "))
    if choice < 5:
        a = int(input("First Number: "))
        b = int(input("Second Number: "))
        if choice == 1:
            print("Answer: " + str(Add(a,b)))
        elif choice == 2:
            print("Answer: " + str(Sub(a,b)))
        elif choice == 3:
            print("Answer: " + str(Mul(a,b)))
        elif choice == 4:
            print("Answer: " + str(Div(a,b)))
    elif choice == 5:
        a = int(input("Base: "))
        b = int(input("Exponent: "))
        print("Answer: " + str(Exp(a,b)))
    elif choice == 6:
        a = int(input("Number: "))
        print("Answer: " + str(Fac(a)))

