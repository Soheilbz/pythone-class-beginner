# ماشین حساب ساده


a = int ( input ("enter first number :"))
b = int (input ("enter seccond number :"))

op = input ("please enter youre operation : ")


if op == "+":
    result = a+b 
if op == "-":
    result = a-b 
if op == "*":
    result = a*b 
if op == "/":
    result = a/b 

print ("your result: ", result)
