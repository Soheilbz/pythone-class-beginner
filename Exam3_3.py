#   معادله درجه 2  ax2+bx+c=0
import math
a = float (input ("Enter youre a :"))
b = float (input ("Enter youre b :"))
c = float (input ("Enter youre c :"))
delta = (b*b)-(4*a*c)
if delta > 0 :
    a1 = ((-b)+(math.sqrt(delta)))/(2*a)
    a2 = ((-b)-(math.sqrt(delta)))/(2*a)
    result = ("Answer 1 : ", a1 , "Answer2 : ", a2)
elif delta == 0 :
    result = (-b)/(2*a)
elif delta <0 :
    result = "No Answer"
print (result)