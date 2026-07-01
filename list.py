Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list[]
a=[2,5.6,"python",6+9j,True,False]
print(a)
[2, 5.6, 'python', (6+9j), True, False]
type(a)
<class 'list'>
b=5
type(b)
<class 'int'>
c=[5]
type(c)
<class 'list'>
#append()
a=["python","java","c","c++"]
a.append("DSA")
a
['python', 'java', 'c', 'c++', 'DSA']
a.append("ML","AI")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a.append("ML","AI")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ML","AI"])
a
['python', 'java', 'c', 'c++', 'DSA', ['ML', 'AI']]
#extend()
a=["ML","AI","DSA"]
a.extend(["c","c++","python"])
a
['ML', 'AI', 'DSA', 'c', 'c++', 'python']
#insert()
b=["vja","hyd"]
b.insert(1,"vzg")
b
['vja', 'vzg', 'hyd']
#copy()
a=["black","orange","blue","white"]
a.index("white")
3
a.copy()
['black', 'orange', 'blue', 'white']
b=a.copy()
b
['black', 'orange', 'blue', 'white']
b.count("blue")
1
#sort()
a=["grapes","banana","orange","apple"]
a.sort()
a
['apple', 'banana', 'grapes', 'orange']
b=[8,6,7,4,2,15,9,3,4]
b.sort()
b
[2, 3, 4, 4, 6, 7, 8, 9, 15]
#reverse()
a=[7,8,4,5,6,1,2,9]
a.reverse()
a
[9, 2, 1, 6, 5, 4, 8, 7]
b=["java","html","css"]
b.reverse()
b
['css', 'html', 'java']
#pop()
a=["c","c++","python","java"]
a.pop()
'java'
a
['c', 'c++', 'python']
a.pop("c++")
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a.pop("c++")
TypeError: 'str' object cannot be interpreted as an integer
>>> a
['c', 'c++', 'python']
>>> a.pop(1)
'c++'
>>> a
['c', 'python']
>>> #remove()
>>> a.remove("c")
>>> a
['python']
>>> #examples
>>> a=["vinod","vijay","deva","suraj"]
>>> len(a)
4
>>> b="vinod"
>>> len(b)
5
>>> c=["vinod"]
>>> len(c)
1
>>> #clear()
>>> a.clear()
>>> a
[]
>>> b=[]
>>> b.append("hi")
>>> b
['hi']
