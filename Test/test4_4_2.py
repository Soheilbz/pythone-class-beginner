#  فروشگاه 
produce = []
def read_file () :
    my_file = open ("text4_4_1.txt" , "r")
    for line in my_file :
        result = line.split(",")
        my_dic = {"id" : result[0] , "name" : result[1] , "price" : result[2] , "count" : result[3]}
        produce.append (my_dic)
        # print (my_dic)
read_file ()
# print (produce)

def Show_menu () : 
    print ("1- add")
    print ("2- reamove")
    print ("3- search")
    print ("4- edit")
    print ("5- show  list")
    print ("6- buy")
    print ("7- exit")
def add () :
    id = input ("Enter id : ")
    name = input ("Enter name : ")
    price = input ("Enter price : ")
    count = input ("Enter count : ")
    buyer_dic = {"id" : id , "name" :name , "price" : price, "count" :count}
    produce.append (buyer_dic)
    print (produce)
def reamove () :
    ...
def search () :
    key = input ("enter produce id or name : ")
    for produce in produce :
        if produce["id"] == key or produce["name"] == key :
            print (produce)
            break
    else :
        print ("not found")
def edit () :
    ...
def show_list () :
    print ("id\tname\tprice\tcount")
    # for produce in produce : 
    #     print (produce["id"], "\t" , produce["name"], "\t" , produce["price"], "\t" , produce["count"])
def buy () :
    ...
def save_to_database () : 
    ...


while True : 
    Show_menu ()
    user_choice = int (input ("Choose youre operation : "))

    # while True :
    if user_choice ==1 :
        add ()
    elif user_choice ==2 :
        reamove ()
    elif user_choice ==3 :
        search ()
    elif user_choice ==4 :
        edit ()
    elif user_choice ==5 :
        show_list ()
    elif user_choice ==6 :
        buy ()
    elif user_choice ==7 :
        save_to_database ()
        exit (0)                                                               #  یکی از توابع خود پایتون برای خروج از شرط
    else :
        print ("choose right number ")


