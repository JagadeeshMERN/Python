Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#bitwise operators
#(&=AND)
a=2
b=4
a&b
0
#"bin" is the in-built function in python for binary values
bin(2)
'0b10'
bin(4)
'0b100'
bin(5)
'0b101'
a=2
b=4
a&b
0
a=5
b=7
a&b
5
#OR
#Two 1's and Two opposites value will be 1
a=3
b=6
bin(3)
'0b11'
bin(6)
'0b110'
>>> a|b
7
>>> #~(Negotiation)
>>> #-(x+1) is the formula.
>>> x=5
>>> -(x+1)
-6
>>> ~x
-6
>>> a=9
>>> ~a
-10
>>> #XOR
>>> #Same:0,Opp:1
>>> a=3
>>> b=5
>>> a^b
6
>>> a=7
>>> b=9
>>> a^b
14
>>> #Left shift
>>> a=3
>>> a<<2
12
>>> #Right shift
>>> a=5
>>> a>>2
1
