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
