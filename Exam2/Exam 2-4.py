# جمع نا محدود اعداد 
num1= float (input ("Enter youre number : "))
list1 = []
list1.append (num1)
while True :
    num2 = input ("Enter yore number to sum or exit : ")
    if num2 == "exit" :
        break
    c = float (num2)
    if num2 !="exit" :
        listnumber = len (list1)
        result = list1[listnumber-1]+c
        list1.append (result)
        print ("youre sum : ", result)