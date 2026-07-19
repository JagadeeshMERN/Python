#functions
'''a=10
b=20
print("The sum is:",a+b)
print("The differ is:",a-b)
print("The product is:",a*b)
a=100
b=200
print("The sum is:",a+b)
print("The differ is:",a-b)
print("The product is:",a*b)
a=1000
b=2000
print("The sum is:",a+b)
print("The differ is:",a-b)
print("The product is:",a*b)'''

'''def calculate(a,b):
    print("The sum is:",a+b)
    print("The differ is:",a-b)
    print("The product is:",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''

'''def calculate(a,b):
    print("The integer division is:",a//b)
    print("The power value is:",a**b)
    print("The modulus is:",a%b)
calculate(18,2)'''


'''def add(a,b):
    print(a+b)
add(4,5)'''

'''while True:
    def cal():
        a=int(input("Enter a number:"))
        b=int(input("Enter a number:"))
        print(a+b)
    cal()'''


'''def cal():
    a=int(input("a value:"))
    b=int(input("b value:"))
    print(a+b)
    cal()
cal()'''

'''
def fullname():
    fname=input("First Name:")
    lname=input("Last Name:")
    print((fname+" "+lname).title())
fullname()'''

'''def mul(a,b):
    print(a*b)
mul(15,3)'''

'''def mul(a,b):
    return a*b
print(mul(2,3))'''

#print v/s return
'''def add(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
add(5,6)'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e
print(cal(5,7))'''

#splitbill()
'''def bill():
    bill_amount=int(input("Enter the amount:"))
    persons=int(input("No: of persons per table:"))
    total=bill_amount/persons
    print(total)
bill()'''

'''def bill():
    bill_amount=int(input("Enter the amount:"))
    persons=int(input("No: of persons per table:"))
    total=bill_amount//persons
    print("Per head bill is {}".format(total))     #[.format]
    print(f"{bill_amount} is the total amount.\nThe amount to be shared among {persons} persons is {total}")    #[f-string]
bill()'''


'''def cal(a,b):
    a=int(input("Enter the value of a:"))
    b=int(input("Enter the value of b:"))
    option=int(input("Select the option:"))
    if option==1:
        print("The sum is:",a+b)
    elif option==2:
        print("The differ is:",a-b)
    else:
        print("The product is:",a*b)     
cal(5,10)'''


#single def keywords()
'''def cal():
    a=int(input("Enter value of a:"))
    b=int(input("Enter value of b:"))
    option=int(input(conditions.py
                         1.add
                         2.sub
                         3.mul))
    if option==1:
        print(a+b)
    elif option==2:
        print(a-b)
    elif option==3:
        print(a*b)
cal()'''


#multiple def keyword()
'''def add():
    print(a+b)

def sub():
    print(a-b)

def mul():
    print(a*b)

while True:
    a = int(input("a value: "))
    b = int(input("b value: "))

    option = int(input(choose the option:
1.add
2.sub
3.mul))

    if option == 1:
        add()
    elif option == 2:
        sub()
    elif option == 3:
        mul()'''


#keyword and positional arguments
'''def Details(id,name,mailid):
    id=37
    name="jagadeesh"
    mailid="jagadeesh672@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''


'''def Details(id,name,mailid):
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id=10,name="jagadeesh",mailid="j@gmail.com")
Details(id=20,name="vignesh",mailid="v@gmail.com")
Details(id=30,name="sainadh",mailid="s@gmail.com")
Details(40,"trinadh","t@gmail.com")
Details("k@gmail.com","kailash",50)
Details(mailid="r@gmail.com",id=60,name="rohit")'''


#default arguments() - 4 steps
'''def Grocery(item,price):
    print("Item is %s" %item)
    print("Price is %.f" %price)
Grocery("Sugar",100)'''

'''def Grocery(item="Rice",price=1500):
    print("Item is %s" %item)
    print("Price is %.f" %price)
Grocery()'''

'''def Grocery(item,price=200):
    print("Item is %s" %item)
    print("Price is %.f" %price)
Grocery("Dhal")'''

'''def Grocery(item="ghee",price):
    #non def arg follows def arg
    print("Item is %s" %item)
    print("Price is %f" %price)
Grocery(500)'''


#Bakery()
'''def bakery(cake_name,price,qty):
    print("Item is %s cake." %cake_name)
    print("Price of cake is %.f." %price)
    print("Quantity of cake is %d." %qty)
bakery("Chocolate",650,1)'''

'''def bakery(cake_name="Redvelevet",price=1000,qty=1):
    print("Item is %s cake." %cake_name)
    print("Price of cake is %.f." %price)
    print("Quantity of cake is %d." %qty)
bakery()'''

'''def bakery(cake_name,price=850,qty=2):
    print("Item is %s cake." %cake_name)
    print("Price of cake is %.f." %price)
    print("Quantity of cake is %d." %qty)
bakery("Chocolate")'''

'''def bakery(cake_name="strawberry",price,qty):
    print("Item is %s cake." %cake_name)
    print("Price of cake is %.f." %price)
    print("Quantity of cake is %d." %qty)
bakery(price=650,qty=1)'''
    
#variable length arguments
'''def check(*a):
    print(a)
    print(type(a))
check()
check(2,3,4,5,6,7,8)
b=[4,5,6,7,8]
check(*b)
c={5,6,7,8,9,10}
check(*c)
d={"name":"jagadeesh","age":22,"place":"vja"}
check(*d)'''

'''def check1(*a):
    d=1#creating a variable
    print(a)
    print(type(a))
    for i in a:
        d=d+1
        print(d)
check1()
check1(2,3,4,5,6)
check1(1,3,4,5,2.3,4.3)
check1(4,3,6,2,3.4,2.3,"python")'''


'''def check1(*a):
    d=1#creating a variable
    print(a)
    print(type(a))
    for i in a:
        #if type(i)==int or type(i)==float:
        if type(i) in (int,float):
            d=d+1
            print(d)
check1()
check1(2,3,4,5,6)
check1(1,3,4,5,2.3,4.3)
check1(4,3,6,2,3.4,2.3,"python")'''

#**(kwargs)
'''def check2(**a):
    print(a)
    print(type(a))
check2()
details={"names":["jagadeesh","vinod","ajay"],
         "marks":[60,70,80],
         "status":["p","a","p"]}
check2(**details)'''


'''def check2(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(i)
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)       
check2()
details={"names":["jagadeesh","vinod","ajay"],
         "marks":[60,70,80],
         "status":["p","a","p"]}
check2(**details)'''

#both * and ** usage
'''def final(*a,**b):          #*=tuple(),**=dict{}
    d=2
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("Key is:",i)
        print("Value is:",j)

final()
data=(2,3,4,5,6,2.3,4.5)
final(*data)
details={"year":[2024,2025,2026],
         "month":["june","july","august"]}
final(**details)
final(*data,**details)'''



            
        
    



   


