def addition(number1,number2):
    Result_Add=number1+number2
    print(Result_Add)

def subtraction(number1,number2):
    Result_Sub=number1-number2
    print(Result_Sub)

def multiply(number1,number2):
    Result_mult=number1*number2
    print(Result_mult)

def division(number1,number2):
    Result_div=number1/number2
    print(Result_div)

Operator_Input=""

while Operator_Input != "e":
    Operator_Input=input("""
    Hello and welcome to the calculator.
    
    Press a for addition
    Press s for subtraction
    Press m for multiplication
    Press d for division
    Press e to exit the program

    Please enter a letter, then press enter:  """)
    if (Operator_Input=="a"):
        number1=int(input("Enter the first number: "))
        number2=int(input("Enter the second number: "))
        print("\n",number1,"+",number2,"is: ")
        addition(number1,number2)
    elif (Operator_Input=="s"):
        number1=int(input("Enter the first number: "))
        number2=int(input("Enter the second number: "))
        print("\n",number1,"-",number2,"is: ")
        subtraction(number1,number2)
    elif (Operator_Input=="m"):
        number1=int(input("Enter the first number: "))
        number2=int(input("Enter the second number: "))
        print("\n",number1,"x",number2,"is: ")
        multiply(number1,number2)
    elif (Operator_Input=="d"):
        number1=int(input("Enter the first number: "))
        number2=int(input("Enter the second number: "))
        while (number2==0):
            print("You cannot divide by 0. Please try again: ")
            number2=int(input("Enter the second number: "))
        print("\n",number1,"/",number2,"is: ")
        division(number1,number2)
    elif (Operator_Input=="e"):
        print("\n You have exited the program. Goodbye :) ")
    else:
        print("\n That is not an option smartass")

