import math  

def main():

    A = int(input("write the first number: "))
    B = int(input("write the second number: "))

    C = pythag(A, B)
    print(f"The length of the hypotenuse is {C}")

def pythag(A,B):

    return math.sqrt(A**2 +B**2)

main()
