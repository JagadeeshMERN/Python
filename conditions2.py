#multiple-if conditions
'''a=20
b=40
if a<b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("not equal")'''

'''a=20
b=40
if a==b:
    print("less")
if b>a:
    print("greater")
if a!=b:
    print("not equal")'''

'''
a=20
b=40
if a==b:
    print("less")
if b>a:
    print("greater")
if a>=b:
    print("not equal")
else:
    print("true")'''

#nested-if conditions
'''a=4
b=9
if a<b:
    print("less")
    if b>a:
        print("greater")'''

'''a=4
b=9
if a<b:
    print("less")
    if b>a:
        print("greater")'''

'''a=7
b=11
if a!=b:
    print("true")
    if b==a:
        print("false")'''

'''a=7
b=11
if a!=b:
    print("true")
    if b==a:
        print("equal")
    else:
        print("not equal")'''

'''a=13
b=15
if a==b:
    print("false")
    if b>a:
        print("true")
else:
    print("False")'''

'''a=7
b=11
if a!=b:
    print("true")
    if b==a:
        print("False")
    else:
        print("True")
else:
    print("not true")'''

a=int(input())
b=int(input())
if a!=b:
    print("true")
    if b==a:
        print("equal")
    elif b>a:
        print("greater")
    else:
        print("false")
else:
    print("program ends")
