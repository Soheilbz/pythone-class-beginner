#   شطرنجی با ابعاد n * m 
def chess () :
    x = int (input("Enter yore row : "))
    y = int (input ("Enter youre column :"))
    a = " "
    b = " "
    for i in range (x) :
        if i%2 == 0: 
            a += "⬜"
            b += "⬛"
        else:
            a += "⬛"
            b += "⬜"
    for i in range(y): 
        if i%2 == 0:
            print(a)
        else:
            print(b)
chess()