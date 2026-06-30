Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#escape sequences
#\n->new line
#\t->tab space (4 to 8 between)
a="name\nmobile\tmailid\nclg"
print(a)
name
mobile	mailid
clg
b="name:jagadeesh\nmobileno:9876545678\tmailid:jagadeesh@gmail.com\nclg:Vignan"
print(b)
name:jagadeesh
mobileno:9876545678	mailid:jagadeesh@gmail.com
clg:Vignan
>>> #replace()
>>> a="wait until you succeed"
>>> a.replace("wait","work")
'work until you succeed'
>>> a
'wait until you succeed'
>>> b="wait wait until you succeed"
>>> b.replace("wait","work")
'work work until you succeed'
>>> b.replace("wait","work",1)
'work wait until you succeed'
>>> #upper()
>>> a="hello"
>>> a.upper()
'HELLO'
>>> #lower()
>>> b="HI"
>>> b.lower()
'hi'
>>> c="python"
>>> c[0].upper()
'P'
>>> c.capitalize()
'Python'
>>> a="python course"
>>> a.title()
'Python Course'
>>> c="i am in the class"
>>> c.title()
'I Am In The Class'
