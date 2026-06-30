Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a="java"
>>> a.isupper()
False
>>> a.islower()
True
>>> a.isdigit()
False
>>> a.isalpha()
True
>>> b="python course"
>>> b.isalpha()
False
>>> c="pythoncourse"
>>> c.isalpha()
True
>>> d=1234
>>> d.isdigit()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
>>> d="1234"
>>> d.isdigit()
True
>>> d.isalnum()
True
>>> e="jagadeesh12345"
>>> e.isalnum()
True
>>> f="jagadeesh1234"
f.isnotalnum()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    f.isnotalnum()
AttributeError: 'str' object has no attribute 'isnotalnum'. Did you mean: 'isalnum'?
f="jagadeesh@123"
f.isalnum()
False
a="hello python"
a.startswith("h")
True
a.endswith("n")
True
