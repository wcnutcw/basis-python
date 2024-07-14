# Factorial


"""

5! = 5x4x3x2x1
4! = 4x3x2x1

"""

def Factorial(number):
    if number==1:
        return number
    else:
        return number*Factorial(number-1) 

x=Factorial(8)
print(x)


