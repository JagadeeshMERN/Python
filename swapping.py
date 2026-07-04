#swapping two variables
'''
a=int(input())
b=int(input())
a,b=b,a
print(a)
print(b)'''

#swapping two variables using temp variable
'''
a=10
b=20
temp=a
a=b
b=temp
print(a)
print(b)
'''

#swapping two variables using arithmetic operations
'''
a=10
b=20
a=a+b
b=a-b
a=a-b
print("Value of a is:",a)
print("Value of b is:",b)
'''
#swapping two variables using number formatting
'''a=10
b=20
a=a+b
b=a-b
a=a-b
print("After swapping a=%d,b=%d" %(a,b))'''


'''a=float(input("Enter the value of a:"))
b=float(input("Enter the value of b:"))
a=a+b
b=a-b
a=a-b
print("After swapping a=%.2f,b=%.2f" %(a,b))'''

a=input()
b=input()
a,b=b,a
print("After swapping the values of a=%s,b=%s" %(a,b)) 
