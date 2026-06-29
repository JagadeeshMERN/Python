Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#slicing
a="codegnan"
a[0]+a[1]+a[2]+a[3]
'code'
a[0:3]
'cod'
a[0:4]
'code'
a[4:]
'gnan'
a[:4]
'code'
a[:8]
'codegnan'
b="work until you succeed"
b[0:4]
'work'
b[5:10]
'until'
b[11:14]
'you'
b[0:4]
'work'
b[15:24]
'succeed'
c="codegnan it solutions"
c[9:11]
'it'
>>> c[0:8]
'codegnan'
>>> c[12:20]
'solution'
>>> d="vijayawada is a royal city"
>>> d[-5:-10]
''
>>> d[-6:-10]
''
>>> d[-5:-11]
''
>>> d[-5:]
' city'
>>> d[-10:]
'royal city'
>>> d[-10:-5]
'royal'
>>> d[-5:]
' city'
>>> d[-4:]
'city'
>>> d[-26:-16]
'vijayawada'
>>> e="vizag is city of destiny"
>>> e[-15:-11]
'city'
>>> e[-24:-19]
'vizag'
>>> e[-7:]
'destiny'
