#  برای خواندن اطلاعات یک فایل از r استفاده می کنیم 
# my_file = open ("Test4_3_1.txt" , "r")
# text = my_file.read()
# print (text)

#  برای پاک کردن داده های قبلی و اضافه کردن داده جدید از w استفاده می کنیم
# my_file = open ("Test4_3_1.txt" , "w")
# text = my_file.write("hi my fiend , you are best")
# print (text)

#  برای پاک نشدن محتویات قبلی و اضافه کردن داده جدید از a استفاده می کنیم 
my_file = open ("Test4_3_1.txt" , "a")
text = my_file.write("\nhi my fiend , you are best")
print (text)
