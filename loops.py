#loops()
#for,while,range,break,continue,pass
#for loop()

#using int
'''a=[10,20,30,40,50]
for i in a:
    print(i)'''

'''a=[10,20,30,40,50]
for i in a:
    print(a)'''

'''a=[10,20,30,40,50]
for i in a:
    print(i,end=",")'''

'''a=[10,20,30,40,50]
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a=(5,6,7,8,9)
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''a={5,6,7,8,9}
for i in a:
    print(i)
print(type(a))
print(type(i))'''

'''b={"year":2026,"month":"july","date":9}
for i in b:
    print(i)
    print(type(b))
    print(type(i))
for i in b.keys():
    print(i)
    print(type(b))
    print(type(i))
for i in b.values():
    print(i)
    print(type(b))
    print(type(i))
for i in b.items():
    print(i)
    print(type(b))
    print(type(i))'''

#using str
'''b="codegnan"
for i in b:
    print(i)'''

#using float
'''b=[4.5,6.7,8.9]
for i in b:
    print(i)
    print(type(b))
    print(type(i))'''
    
#using complex
'''b=[4+5j,8+9j]
for i in b:
    print(i)
    print(type(b))
    print(type(i))'''

#using bool
'''b=[True,False]
for i in b:
    print(i)
    print(type(b))
    print(type(i))'''


#example
'''fruits=["apple","banana","mango"]
for i in fruits:
    print(i.upper(),end=" ")

b=[]
for i in fruits:
    b.append(i.upper())
print(b)'''

'''a=[1,3,5,7,9,"code"]
#[1,3,5,7,9,"c","o","d","e"]
a.extend("code")
print(a)'''


#while loop
'''a=10
while a>1:
    print(a)'''

'''a=10
while a<1:
    print(a)'''

'''a=10
while a>1:
    print(a)
    a=a-1'''

'''a=10
while a>=1:
    print(a)
    a=a-1'''

'''a=20
while a>3:
    print(a)
    a=a-1'''

'''a=20
while a>5:
    a=a-1
print(a)'''

'''a=40
while a>5:
    print(a)
    a-=1'''

'''a=30
while a>1:
    print(a)
    a+=1'''

'''a=10
while a>2:
    print(a)
    a-=1'''

'''a=30
while a>1:
    print(a)
    a-=1'''

'''a=1
while a<25:
    print(a)
    a+=1'''

#vote using while loop
'''while True:
    age=int(input("Enter your age:"))
    if age>=18:
        print("You are eligible for vote.")
    else:
        print("You are not eligible for vote")'''

#even_odd using while loop
'''while 1:
    num=int(input("Enter the number:"))
    if num%2==0:
        print(f"The {num} is Even.")
    else:
        print(f"The {num} is Odd.")'''

#range()
#The range function written in sequence of numbers, starting from zero by default and increments one by one and stops before specified number.
#start-stop-step

'''for i in range(20):
    print(i)'''

'''for i in range(13,35):
    print(i)'''

'''for i in range(0,30,3):
    print(i,end=",")'''

'''for i in range(5,50,5):
    print(i)'''

'''for i in range(2,20,2):
    print(i)'''

#Grades
'''while True:
    marks=int(input("Enter your marks:"))
    if marks in range(91,101):
              print("Grade A")
    elif marks in range(81,91):
              print("Grade B")
    elif marks in range(70,81):
        print("Grade C")
    elif marks in range(50,71):
        print("Grade D")
    else:
        print("Fail")'''

#break
'''a=10
while a>1:
    print(a)
    a=a-1'''

'''a=10
while a>1:
    print(a)
    a=a-1
    if a==6:
        break'''

'''a=10
while a>1:
    a=a-1
    if a==6:
        break
    print(a)'''

'''for i in range(20):
    if i==13:
        break
    print(i)'''

'''a="python"
if a=="n":
    break
print(i)''' #error

'''a="python"
for i in a:
    if i=="h":
        break
    print(i)'''

#continue
'''a=20
while a>5:
    print(a)
    a=a-1'''

'''a=20
while a>5:
    print(a)
    a=a-1
    if a==10:
        continue'''

'''a=20
while a>5:
    a=a-1
    if a==10:
        continue
    print(a)'''

'''for i in range(15):
    if i==7:
        continue
    print(i)'''

'''a="python"
for i in a:
    if i=="y":
        continue
    print(i)'''


#pass
'''a=30
while a>10:
    print(a)
    a-=1
    if a==20:
        pass'''

'''for i in range(40):
    if i==10:
        pass
    print(i)'''









