# report 
Name = input ("enter student name : ")
Family = input ("enter student family : ")
les1 = float (input ("enter score : "))
les2 = float (input ("enter score : "))
les3 = float (input ("enter score : "))
avs = ((les1+les2+les3)/3)
if avs<=20 and avs>=17 and 20>=les1>=0 and 20>=les2>=0 and 20>=les3>=0:
    result = "Greate"
elif avs<17 and avs>=12 and 20>=les1>=0 and 20>=les2>=0 and 20>=les3>=0: 
    result = "Normal"
elif avs<12 and avs>=0 and 20>=les1>=0 and 20>=les2>=0 and 20>=les3>=0:
    result = "Fail" 
else :
    result = "youre numbers incorrect" 
print ("student average score : " , avs , "\nstudent sondition : ", result)