# نوشتن معادله درجه اول 
# m * x + b = 0 

# def degree1 () :
#     m = float (input ("Enter youre (m) in m * x + b = 0  : "))
#     b = float (input ("Enter youre (b) in m * x + b = 0  : "))
#     x = (-b)/m
#     print (x)

# degree1 ()

# برگرداندن مقدار از تابع با return است
# با return میشه مقدار برگردانده شده رو در جاهای دیگه استفاده کرد

def degree1 () :
    m = float (input ("Enter youre (m) in m * x + b = 0  : "))
    b = float (input ("Enter youre (b) in m * x + b = 0  : "))
    x = (-b)/m
    return x

result = degree1 ()
print ("result : " , result)
