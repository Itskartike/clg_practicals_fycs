#funtion to print addition with or without arguments


#without argument
def sum():
    num1=int(input("Enter  first number:"))
    num2=int(input("Enter second number:"))
    sum=num1+num2
    print("Addition is:",sum)
sum()
#with Arguments
def sum1(x,y):
    sum=x+y
    print("Addition is",sum)    
num1=int(input("Enter  first number:"))
num2=int(input("Enter second number:"))
sum1(num1,num2)
