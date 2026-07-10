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

a=[1,3,5,7,9,"code"]
#[1,3,5,7,9,"c","o","d","e"]
a.extend("code")
print(a)
    
