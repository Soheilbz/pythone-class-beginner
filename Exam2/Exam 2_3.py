# آرایه اعداد تصادفی
import random
n = int (input ("Enter youre list number (n) : "))
array = [] 
while len(array) < n :
    num = random.randint (1,n)
    if num not in array :
        array.append(num)
print (array)