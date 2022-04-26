def division(number1,number2):
    Result_div=number1/number2
    print(Result_div)

number1=int(input("Enter first number: "))
number2=int(input("Enter second number: "))

try:
    division(number1,number2)
except ZeroDivisionError:
    print("cannot divide by zero")
