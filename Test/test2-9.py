# تکرار بی نهایت با while

import random 
pcnumber = random.randint (0,20)

while True :
    usernumber = int(input("Enter youre geuss number : "))
    if pcnumber == usernumber :
        print("youre win")
        break
    elif pcnumber>usernumber :
        print("Go up")
        # if i==2 :
        #     print ("Yore loose")
    elif pcnumber<usernumber :
        print("Go down")
        # if i==2 :
        #     print ("Yore loose")
            