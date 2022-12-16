# ماشین حساب تکرار پذیر 

import math

for i in range (10): 
    a =  float(input ("Enter youre first number : "))
    op = input ("+  -  *  /  sin  cos  tan  cot  root  factorial \nChoose youre operation : ")
    b = math.radians(a)
    if op=="sin" or op=="cos" or op=="tan" or op=="cot" or op=="root" or op=="Factorial" :
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
            if a=="0" or a=="180" or a=="360" :
                result = "Undefind"
            else :
                result = (1/math.tan(b))
        if op == "factorial" :
            result = math.factorial(int(a))
        if op == "root" :
            result = math.sqrt(a)
    else :
        d = float (input ("Enter youre seccond number : "))
        if op == "+" :
            result = a+d 
        if op == "-" :
            result = a-d 
        if op == "*" :
            result = a*d 
        if op == "/" :
            result = a/d 
    print ("youre result :" , result)