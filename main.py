print("           Calculator               ")

num1 = input("Enter number : ")
num2 = input("Enter another number : ")
oper = input("Enter your operation : ")

if oper == '+':
    result = float(num1) + float(num2)
    print("Answer : " + str(result))
elif oper == '-':
    result = float(num1) - float(num2)
    print("Answer : " + str(result))
elif oper == '*':
    result = float(num1) * float(num2)
    print("Answer : " + str(result))
elif oper == '/':
    result = float(num1) / float(num2)
    print("Answer : " + str(result))
else:
    print("Invalid operation")
