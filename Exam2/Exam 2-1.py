# چاپ تعداد حدس کاربر
import random
a = random.randint (0,20)
for number in range (5) :
    print ("youre limit : ", 5-number)
    b = int (input("Enter youre guess : "))
    if a==b :
        print ("you win","\nnumber of try : ", number+1)
        break
    elif a>b :
        if number<4 :
            print ("Choose higher number")
        else :
            print ("your faile this mission")
    elif a<b :
        if number<4 :
            print ("choose lower number")
        else :
            print ("your faile this mission")