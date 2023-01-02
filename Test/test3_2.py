# استفاده از تابع با def
# تابع ها برای تکرار ها کاربردی تر از while و for هستند

#حالت اولیه برای نوشتن این کد
name = input ("Enter youre name : ")
print ("welcome ", name)

#استفاده از تابع در نوشتن کد
def welcome (name):
    print ("welcome " , name)

# welcome ("ali")              # حالت ساده چاپ اسم علی در تابع

for i in range (4):
    b = input ("Enter youre name : ")
    welcome (b)

while True :
    b = input ("Enter youre name : " )
    welcome (b)

# ممکنه تابع ما بدون ورودی کاری رو انجام بده
def sayhello () :
    print("hello")
sayhello ()    