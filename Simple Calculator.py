#Lennard Javier
#the comments are for my smooth brained self
from operator import eq
from re import T, X
from tkinter import Y

def add(x, y):
    eq = x + y #eq is as simple as a variable
    return eq
        
def subtract(x, y):
    eq =  x - y
    return eq

def multiply(x, y):
    eq = x * y
    return eq

def divide(x, y):
    eq = x / y
    return eq

def sqrt(x, y):
    eq = x ** y
    return eq

def main(): #this function sets up the main code
    while True:
        print ("Welcome to the Simple Calculator!")
        print ("Select Operation: \n 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide \n 5. Powered by")

        choice = input("Enter choice:")

        if choice in ('1', '2', '3', '4', '5'): #don't forget about nested ifs
            num1 = float(input("Enter first number: "))
            num2 = float(input ("Enter second number: "))

            if choice == '1':
                eq = add(num1, num2) #this sets up what is defined as x and y
                add(num1, num2)
                print(eq)   
                answer = input("Do you still need a calculator?\n")
                if answer == 'yes':
                    main ()
                else:
                    break

            elif choice == '2':
                eq = subtract(num1, num2)
                subtract(num1, num2)
                print(eq)
                answer = input("Do you still need a calculator?\n")
                if answer.lower() == 'yes':
                    True == True
                    main()
                else:
                    break

            elif choice == '3':
                eq = multiply(num1, num2)
                divide(num1, num2)
                print(eq)
                answer = input("Do you still need a calculator? \n")
                if answer.lower() == 'yes':
                    True == True
                    main()
                else:
                    break

            elif choice == '4':
                eq = divide(num1, num2)
                divide(num1, num2)
                print(eq)
                answer = input("Do you still need a calculator?\n")
                if answer.lower() == 'yes':
                    True == True
                    main()
                else:
                    break
            
            elif choice == '5':
                eq = sqrt(num1, num2)
                sqrt(num1, num2)
                print(eq)
                answer = input("Do you still need a calculator? \n")
                if answer.lower() == 'yes':
                    True == True
                    main()
                else:
                    break

main() #this calls up the function