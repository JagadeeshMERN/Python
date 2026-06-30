Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#formatting
a=4
b=6
print(a+b)
10
print("The sum of a&b is:",a+b)
The sum of a&b is: 10
#format method
>>> a="vinod"
>>> b="ajay"
>>> print("Hello",a+b)
Hello vinodajay
>>> print("Hello {}{}.format(a,b))
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("hello {}{}".format(a,b))
...       
hello vinodajay
>>> print("hello {} hello {}".format(a,b))
...       
hello vinod hello ajay
>>> #fstring
...       
>>> a="sita"
...       
>>> b="ram"
...       
>>> print(f "Hello {a}{b}")
...       
SyntaxError: invalid syntax
>>> print(f"Hello {a}")
...       
Hello sita
>>> print(f"Hello {b}")
...       
Hello ram
>>> print(f"Hello {a},Hello {b}")
...       
Hello sita,Hello ram
