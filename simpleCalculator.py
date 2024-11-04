def calculator(num1,num2,opr):
    if (opr=='+'):
        return num1+num2
    elif(opr=='-'):
        return num1-num2
    elif (opr=='*'):
        return num1*num2
    elif (opr=='/'):
        if (num2==0):
            print("ERROR : Division by zero is not allowed")
        else:
            return num1/num2
    elif (opr=='%'):
        return num1%num2
try:
    firstnumber = float(input("Enter the First Number :"))
    secondnumber = float(input("Enter the Second Number :"))
    print("Choose an Operator : +,-,/,*,%")
    operator = input("Enter the Operator : ")
    print("Result : ",calculator(firstnumber,secondnumber,operator))
except ValueError:
    print("Invalid Input! Please enter numeric values for numbers ")