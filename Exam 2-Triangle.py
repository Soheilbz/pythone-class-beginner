# Triangle
a = float (input ("enter first side : "))
b = float (input ("enter seccound side : "))
c = float (input ("enter third side : "))
aa = b+c
bb = b+a
cc = a+b
if a<aa and b<bb and c<cc :
    result = "Availible"
elif a==0 or b==0 or c==0 :
    result = "youre number inccorect"
else :
    result = "not Availible"
print ("youre result : ", result)