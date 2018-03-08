#Addition
def add(a, b):
    return (a + b)

#Subtraction
def sub(a, b):
    return (a - b)

#Multiplication
def mul(a, b):
    return (a * b)

#Division
def div(a, b):
    return (a / b)

#Exponent
def exp(a, b):
    result = 1
    if b == 0:
        return 1
    while b > 0:
        result = result*a
        b -= 1
    return result

#Factorial
def fac(a):
    result = a
    i = 1
    if a == 0 or a == 1:
        return 1
        # only the factorial of 1 and 0 can equal 1
    else:
        while i < a:
            result = i*result
            i += 1
            # i increases and multiplies it by a number bigger until it reaches the entered number
        return result 
choice = 0
#while the user does not what to exit
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
    #Finding the user's choice
    choice = int(input("Your Choice: "))
    #If the choice is within the four basic functions
    if choice < 5:
        a = int(input("First Number: "))
        b = int(input("Second Number: "))
        if choice == 1:
            print("Answer: " + str(add(a,b)))
        elif choice == 2:
            print("Answer: " + str(sub(a,b)))
        elif choice == 3:
            print("Answer: " + str(mul(a,b)))
        elif choice == 4:
            print("Answer: " + str(div(a,b)))
    #else if the choice is 5(exponent)
    elif choice == 5:
        a = int(input("Base: "))
        b = int(input("Exponent: "))
        print("Answer: " + str(exp(a,b)))
    #else if the choice is 6(factorial
    elif choice == 6:
        a = int(input("Number: "))
        print("Answer: " + str(fac(a)))

