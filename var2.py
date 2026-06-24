Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=4;b=9
print(a+b)
13
a,b,c=4,5,6
print(a+b-c)
3
a=b=c=15
print(a,b,c)
15 15 15
print(a+b+c)
45
a,b,c=2,3,4,5,6,7,8
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a,b,c=2,3,4,5,6,7,8
ValueError: too many values to unpack (expected 3, got 7)
a,b,c=2,3,4
print(a,b,c)
2 3 4
a,b,c=(3,4,5)
print(a,b,c)
3 4 5
print(abc)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(abc)
NameError: name 'abc' is not defined. Did you mean: 'abs'? Or did you forget to import 'abc'?
first name="jagadeesh"
SyntaxError: invalid syntax
first_name="jagadeesh"
last_name="parasa"
print(first_name+last_name)
jagadeeshparasa
print(first_name+" "+last_name)
jagadeesh parasa
fname="jagadeesh"
lname="parasa"
print(fname+lname)
jagadeeshparasa
pritn(fname+" "+lname)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    pritn(fname+" "+lname)
NameError: name 'pritn' is not defined. Did you mean: 'print'?
print(fname+" "+lname)
jagadeesh parasa
print(fname,lname)
jagadeesh parasa
#case sensitive
>>> name="jagadeesh"
>>> print(name)
jagadeesh
>>> print(Name)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(Name)
NameError: name 'Name' is not defined. Did you mean: 'name'?
>>> print(NAME)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print(NAME)
NameError: name 'NAME' is not defined
>>> Name="Vinod"
>>> print("Name")
Name
>>> print(Name)
Vinod
>>> #delete keyword
>>> a=45
>>> print(a)
45
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
