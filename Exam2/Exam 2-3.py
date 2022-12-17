# آرایه اعداد تصادفی
import random
n = int (input ("Enter youre list number (n) : "))
r = n
list1 = [] 
listnumber = len(list1)
while listnumber <= n:
    num = random.randint (1,r)
    if num in list1 :
        n=n
    else :
        list1.append (num)
    listnumber +=1
print (list1)