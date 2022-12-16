# ساخت بازی حدس زدن عدد
# کتابخانه اعداد تصادفی در پایتون random است


import random 
pcnumber = random.randint (0,20)

for i in range (3):
    usernumber = int(input("Enter youre geuss number : "))
    if pcnumber == usernumber :
        print("youre win")
        break
    elif pcnumber>usernumber :
        print("Go up")
        if i==2 :
            print ("Yore loose")
    elif pcnumber<usernumber :
        print("Go down")
        if i==2 :
            print ("Yore loose")

