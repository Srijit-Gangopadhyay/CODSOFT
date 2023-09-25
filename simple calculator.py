def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2

print("Please the select the operation of your choice: \n" \
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")

choice=int(input("Select operation from 1,2,3,4--"))

number1=int(input("Enter the first number:"))
number2=int(input("Enter the second number:"))

if choice==1:
    print(number1,"+",number2,"=",add(number1,number2))

elif choice==2:
    print(number1,"-",number2,"=",subtract(number1,number2))

elif choice==3:
    print(number1,"*",number2,"=",multiply(number1,number2))

elif choice==4:
    print(number1,"/",number2,"=",divide(number1,number2))


else:
    print("Choice is unknown")