Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatype conversions
#int
int(6)
6
int(4.5)
4
int("code")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int("code")
ValueError: invalid literal for int() with base 10: 'code'
int(3+4j)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    int(3+4j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0

#float
float(5)
5.0
float(5.0)
5.0
float("code")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float("code")
ValueError: could not convert string to float: 'code'
float(6+4j)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    float(6+4j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
#string
str(12)
'12'
str(3.5)
'3.5'
str("code")
'code'
str(6+8j)
'(6+8j)'
str(True)
'True'
str(False)
'False'
>>> #complex
>>> complex(12)
(12+0j)
>>> complex(44.5)
(44.5+0j)
>>> complex("code")
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    complex("code")
ValueError: complex() arg is a malformed string
>>> complex(4+6j)
(4+6j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #boolean
>>> bool(56)
True
>>> bool(-1)
True
>>> bool(4.5)
True
>>> bool("Hi")
True
>>> bool(3+7j)
True
>>> bool(9+5j)
True
>>> bool(0)
False
