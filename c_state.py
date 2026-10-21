# IF statement 
#WAP to check given number is greater then 50
n = int(input("Enter num :"))
if n>50:
    print(f"{n} is Greater then 50") # An f-string (formatted string literal) is a string prefixed with f or F 
                                     #that allows variables and expressions to be embedded directly within the text using curly braces {}. 

# if else statement 
# if conditon is satisfied then if block executes if not then else block executed 
# check number is even or odd
num=int(input("Enter number: "))
if num%2==0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")

#if-elif-else
# to check num is positive or negative 
num1=int(input("Enter number: "))
if num1==0:
    print(f"number is 0")
elif num1>0:
    print(f"{num1} is positive number")
else:
    print(f"{num1} is negative number")

#wap to check the given number us gretest num amoung 3 no 


x = int(input("Enter number1: "))
y = int(input("Enter number2: "))
z = int(input("Enter number3: "))

if x>y and x>z:
    print(f"{x} is greater amoung all")
elif y>x and y>z:
    print(f"{y} is greater amoung all")
else:
    print(f"{z} is greater amoung all")

#wap to given year is leap or not 
year = int(input("enter year eg.(2018 ,2019 etc): "))
if year%400==0 or(year % 4 == 0 and year % 100 !=0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")
