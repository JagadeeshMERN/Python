#conditions
#if-condition by using comparision operators
#<,>,<=,>=,!=,==
'''a=10
b=20
if a<b:
    print("True")'''

'''a=15
b=12
if a>b:
    print("True")'''


'''a=5
b=7
if a<=b:
    print("less")'''


'''a=12
b=15
if a>=b:
    print("True")'''

'''a=10
b=10
if a==b:
    print("True")'''

'''a="python"
if a=="python":
    print("Matched")'''

'''a=int(input("a value:"))
b=int(input("b value:"))
if a<b:
    print("True")'''

'''a=int(input("value of a:"))
if a<50:
    print("True")'''

#if-condition by using logical operators
#and,or,not
'''a=3
b=6
if a<b and b>a:
    print("True")'''

'''a=4
b=7
if a<=b and b>=a:
    print("True")'''

'''a=9
b=12
if a!=b and a==b:
    print("True")'''

'''a=2
b=4
if a<b or b>a:
    print("True")'''

'''a=14
b=16
if a<=b or b>=a:
    print("True")'''

'''a=3
b=6
if a!=b or a==b:
print("True")'''

'''a=5
b=7
if not a<b:
    print("True")'''

'''a=3
b=6
if not a<b and b>a:
    print("True")'''

'''a=3
b=6
if not a<b or b>a:
    print("True")'''

#if-condition by using identify operators
#is,is not

'''a=4
if type(a) is int:
    print("is is int")'''

'''a=4
if type(a) is not int:
    print("is is int")'''

'''a=4.5
if type(a) is float:
    print("is is float")'''

'''a=4.5
if type(a) is not float:
    print("is is float")'''

'''a="python"
if type(a) is str:
    print("is is string")'''

'''a="java"
if type(a) is not str:
    print("is is string")'''

'''a=4+5j
if type(a) is complex:
    print("is is complex")'''

'''a=9+7j
if type(a) is not complex:
    print("is is complex")'''

'''a=True
if type(a) is bool:
    print("is is bool")'''

'''a=False
if type(a) is not bool:
    print("is is bool")'''

#if-condition using membership operators
'''a=2,3,4,5,6,7,8,9
if 8 in a:
    print("True")'''

'''a=2,3,4,5,6,7,8
if 20 not in a:
    print("True")'''

'''a=int(input("a value"))
if 30 in a:
    print("true")'''#error

'''a=2,3,4,5,6,7,8,9,10
b=int(input("value:"))
if b in a:
    print("True")'''

#if-else conditions by using comparision operators
'''a=4
b=8
if a<b:
    print("True")
else:
    print("False")'''

'''a=4
b=7
if a>b:
    print("True")
else:
    print("False")'''

'''a=5
b=10
if a<=b:
    print("True")
else:
    print("False")'''

'''a=5
b=10
if a>=b:
    print("True")
else:
    print("False")'''

'''a=5
b=10
if a!=b:
    print("True")
else:
    print("False")'''

'''a=5
b=10
if a==b:
    print("True")
else:
    print("False")'''
#if-else conditions by using logical operators
'''
a = 5
b = 10
if a < b and b > 5:
    print("True")
else:
    print("False")'''

'''
a = 15
b = 10
if a < b and b > 5:
    print("True")
else:
    print("False")'''

'''
a = 15
b = 10
if a < b or b == 10:
    print("True")
else:
    print("False")'''

'''
a = 20
b = 10
if a < b or b > 20:
    print("True")
else:
    print("
a = 5
if not a > 10:
    print("True")
else:
    print("False")'''

'''
a = 15
if not a > 10:
    print("True")
else:
    print("False")'''

'''
a = 8
b = 8
if a == b and b == 8:
    print("True")
else:
    print("False")'''

'''
a = 5
b = 8
if a == 10 or b == 8:
    print("True")
else:
    print("False")'''

'''
a = 10
if not a == 5:
    print("True")
else:
    print("False")'''

'''
a = 5
b = 10
c = 15
if a < b and b < c and c > 10:
    print("True")
else:
    print("False")'''

'''
a = 20
b = 5
c = 15
if a < b or b > 10 or c == 15:
    print("True")
else:
    print("False")'''

'''
a = 5
b = 10
c = 20
if (a < b and b < c) or c == 10:
    print("True")
else:
    print("False")'''

'''
a = True
b = False
if a and b:
    print("True")
else:
    print("False")'''

'''# 
a = True
b = False
if a or b:
    print("True")
else:
    print("False")'''

'''
a = False
if not a:
    print("True")
else:
    print("False")'''

#if-else conditions by using identify operators
#is,is not
'''
a = 10
b = a
if a is b:
    print("True")
else:
    print("False")'''

'''
a = 10
b = 20
if a is not b:
    print("True")
else:
    print("False")'''

'''
a = 10.5
b = a
if a is b:
    print("True")
else:
    print("False")'''

'''
a = 10.5
b = 20.5
if a is not b:
    print("True")
else:
    print("False")'''

'''# str using is
a = "Python"
b = a
if a is b:
    print("True")
else:
    print("False")'''

'''
a = "Python"
b = "Java"
if a is not b:
    print("True")
else:
    print("False")'''

'''
a = 2 + 3j
b = a
if a is b:
    print("True")
else:
    print("False")'''

'''
a = 2 + 3j
b = 4 + 5j
if a is not b:
    print("True")
else:
    print("False")'''

'''
a = True
b = a
if a is b:
    print("True")
else:
    print("False")'''

'''
a = True
b = False
if a is not b:
    print("True")
else:
    print("False")'''
#if-else conditions by using membership operators
#in,not in
'''
a = [10, 20, 30, 40]
if 20 in a:
    print("True")
else:
    print("False")'''

'''
a = [10, 20, 30, 40]
if 50 not in a:
    print("True")
else:
    print("False")'''

'''
a = [1.1, 2.2, 3.3, 4.4]
if 2.2 in a:
    print("True")
else:
    print("False")'''

'''
a = [1.1, 2.2, 3.3, 4.4]
if 5.5 not in a:
    print("True")
else:
    print("False")'''

'''
a = "Python Programming"
if "Python" in a:
    print("True")
else:
    print("False")'''

'''
a = "Python Programming"
if "Java" not in a:
    print("True")
else:
    print("False")'''

'''
a = [2+3j, 4+5j, 6+7j]
if 4+5j in a:
    print("True")
else:
    print("False")'''

'''
a = [2+3j, 4+5j, 6+7j]
if 8+9j not in a:
    print("True")
else:
    print("False")'''

'''
a = [True, False]
if True in a:
    print("True")
else:
    print("False")'''


a = [True, False]
if None not in a:
    print("True")
else:
    print("False")
