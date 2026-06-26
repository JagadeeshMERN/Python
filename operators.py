Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#operators
#arithmetic operators
a=2
b=4
print(a+b)
6
print(a-b)
-2
print(a*b)
8
print(a//b)
0
print(a/b)
0.5
print(a**b)
16
print(a%b)
2
#assignment operators
a=5
b=3
a+=b
a
8
a-=b
a
5
a*=b
a
15
a//=b
a
5
a/=b
a
1.6666666666666667
a**=b
a
4.629629629629631
a%=b
a
1.6296296296296306
#comparision operators
a=4
b=6
a<b
True
a>b
False
b<A
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    b<A
NameError: name 'A' is not defined. Did you mean: 'a'?
b<a
False
b>a
True
a!=b
True
a==b
False
a<=b
True
a>=b
False
b<=a
False
b>=a
True
#logical operators
a=3
b=6
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a<b or b>a
True
a!=b or a==b
True
a<=b or b<=a
True
>>> not True
False
>>> not False
True
>>> #identity operators
>>> a=4
>>> type(a) is int
True
>>> type(a) is not int
False
>>> b=6.7
>>> type(b) is float
True
>>> type(b) is str
False
>>> type(b) is complex
False
>>> type(b) is bool
False
>>> type(b) is not bool
True
>>> type(b) is not str
True
>>> #membership operators
>>> a=3,4,5,6,7,8,9
>>> 8 in a
True
>>> 20 in a
False
>>> 25 not in a
True
