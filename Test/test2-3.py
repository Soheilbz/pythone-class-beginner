# برنامه یوزر و پسور تکرار پذیر 
# خارج کردن از حلقه با دستور break - اگر کاربر هر بار بخواد بدونه درست یا غلط وارد کرده پرینت باید داخل حلقه باشه


for i in range (5) : 
    use = input("Enter youre username : ")
    pas = input("Enter youre password : ")

    if use=="123" and pas=="1234":
        print ("welcome")
        break
    else :
        print ("enter correct use and pass")
