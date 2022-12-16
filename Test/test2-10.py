#  ماشین حساب بینهایت تکرار پذیر با while 

import math
while True : 
    op = input ("+  -  *  /  sin  cos  tan  cot  root  factorial exit \nChoose youre operation : ")
    if op=="sin" or op=="cos" or op=="tan" or op=="cot" or op=="root" or op=="Factorial" :
        a = float(input ("Enter youre first number : "))
        b = math.radians(a)
        if op == "sin" : 
            result = math.sin(b)
        if op == "cos" : 
            result = math.cos(b)
        if op == "tan" :
            if a=="90" or a=="270":
                result = "Undefind"
            else :
                result = math.tan(b)
        if op == "cot" :
            if a==0 or a==180 or a==360 :
                result = "Undefind"
            else :
                result = (1/math.tan(b))
        if op == "factorial" :
            result = math.factorial(int(a))
        if op == "root" :
            result = math.sqrt(a)
    elif op=="+" or op=="-" or op=="*" or op=="/":
        a = float(input ("Enter youre first number : "))
        d = float (input ("Enter youre seccond number : "))
        if op == "+" :
            result = a+d 
        if op == "-" :
            result = a-d 
        if op == "*" :
            result = a*d 
        if op == "/" :
            result = a/d 
    elif op=="exit" :
        break
    print ("youre result :" , result)