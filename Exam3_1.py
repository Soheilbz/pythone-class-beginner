# 	حذف داده های تکراری وارد شده
mylist = [] 
while True :
    add = input ("Enter your list or exit : ")
    if add != "exit" :
        if add not in mylist :
            mylist.append (add)
    elif add == "exit" : 
        break
print (mylist)

#   حدف داده های تکراری یک لیست از قبل آماده شده
mylist = ["1" , "2" , "3" , "4" , "5" , "2" , "4"]
nonrep = []
for i in range (len(mylist)) :
    if mylist [i] not in nonrep :
        nonrep.append (mylist[i])
print (nonrep)