# تاس
import random
n1 = random.randint (1,6)
print ("youre dice number : " ,n1)
while True : 
    if n1==6 :
        drop = input ("drop youre next dice : y or n  ")
        n2 = random.randint (1,6)
        print ("youre dice number : " ,n2)
        n1=n2
    else :
        break