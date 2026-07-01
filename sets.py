Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#tuple()
a=(4,5.6,"code",9+6j,True,False)
print(a)
(4, 5.6, 'code', (9+6j), True, False)
type(a)
<class 'tuple'>
a.index(True)
4
len(a)
6
#sets{}
a={5,8.9,"vinod",5+9j,True,False}
print(a)
{False, True, (5+9j), 5, 8.9, 'vinod'}
type(a)
<class 'set'>
a={3,4,5,6,7,8}
b={5,6,7,8}
b.issubset(a)
True
a.issuperset(b)
True
a.issubset(b)
False
b.issuperset(b)
True
b.issuperset(a)
False
#union()
a={3,4,5,6,7,8}
b={1,2,3,9,10}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
c={6,7,8,9,10,10,11,8,9}
print(c)
{6, 7, 8, 9, 10, 11}
#intersection()
a={3,4,5,6,7,8,9}
b={6,7,8,9,10,11}
a.intersection(b)
{8, 9, 6, 7}
#update()
a={10,20,30,40,50}
b={40,50,60,70,80}
a.update(b)
a
{70, 40, 10, 80, 50, 20, 60, 30}
b
{80, 50, 70, 40, 60}
b.update(a)
b
{70, 40, 10, 80, 50, 20, 60, 30}
#difference()
a={4,5,6,7,8,9,10,11}
b={3,4,5,6,7,11,12,13}
a.difference(b)
{8, 9, 10}
b.difference(a)
{3, 12, 13}
#symmetric_difference()
a={3,4,5,6,7,8,9}
b={1,3,5,7,8,11,13}
a.symmetric_difference(b)
{1, 4, 6, 9, 11, 13}
#intersection_update()a={}
a={1,3,5,7,9,11,13}
b={2,3,4,6,7,9,11,12}
a.intersection_update(b)
a
{11, 9, 3, 7}
b
{2, 3, 4, 6, 7, 9, 11, 12}
b.intersection_update(a)
b
{3, 9, 11, 7}
#difference_update()
a={2,3,4,5,6,7}
b={9,8,7,5,6,4,2}
a.difference_update(b)
a
{3}
b.difference_update(a)
b
{2, 4, 5, 6, 7, 8, 9}
#symmetric_difference_update
a={11,12,13,14,15,16,17}
b={13,14,15,16,17,18}
a.symmetric_difference_update(b)
a
{18, 11, 12}
b.symmetric_difference_update(a)
b
{16, 17, 11, 12, 13, 14, 15}
#pop()
a={4,5,6,7,8,9,10}
>>> a.pop()
4
>>> a.remove(5)
>>> a
{6, 7, 8, 9, 10}
>>> a.discard(7)
>>> a
{6, 8, 9, 10}
>>> a.copy()
{8, 9, 10, 6}
>>> a
{6, 8, 9, 10}
>>> a.clear()
>>> a
set()
>>> b=set()
>>> b.add(20)
>>> b
{20}
>>> a={3,4,5,6,7}
>>> len(a)
5
>>> a.index(7)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    a.index(7)
AttributeError: 'set' object has no attribute 'index'
>>> a={3,4,5,6,7}
>>> b={8,9,10,11}
>>> a.isdisjoint(b)
True
