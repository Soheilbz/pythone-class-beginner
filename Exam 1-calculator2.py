#calculator
import math
a = float (input ("Enter youre first number : "))
op = input ("+  -  *  /  sin  cos  tan  cot  root  factorial \nChoose youre operation : ")
b = math.radians(a)
if op == "sin" or "cos" or "tan" or "cot" or "root" or "Factorial" :
    if op == "sin" : 
      result = math.sin(b)
    if op == "cos" : 
      result = math.cos(b)
    if op == "tan" :
      result = math.tan(b)
    if op == "cot" :
      result = (1/math.tan(b))
    if op == "factorial" : 
      result = math.factorial(int(a))
    if op == "root" : 
      result = math.sqrt(a)
else :
    d = float (input ("Enter youre first number : "))
    if op == "+" :
      result = a+d 
    if op == "-" :
      result = a-d 
    if op == "*" :
      result = a*d 
    if op == "/" :
      result = a/d 
print ("youre result :" , result)