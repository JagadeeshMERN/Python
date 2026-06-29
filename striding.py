Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="cloud computing"
a[::5]
'c u'
a[::4]
'cdmi'
a[::8]
'cm'
>>> a[2:]
'oud computing'
>>> a[3:11]
'ud compu'
>>> a[::2]
'codcmuig'
>>> a[:2]
'cl'
>>> a[::6]
'cci'
>>> b="machine learning"
>>> b[3:14:2]
'hn eri'
>>> b[5:15:4]
'nei'
>>> b[2:12:3]
'cnlr'
>>> a[0:10:1]
'cloud comp'
>>> b[0:10:1]
'machine le'
>>> c="Python Course"
>>> c[-1:-10:-2]
'ero o'
>>> c[-1:-10:2]
''
>>> c[-3:-13:4]
''
>>> c[-3:-13:-4]
'r t'
