Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #dict{}
>>> a={"name":"Jagadeesh","city":"Guntur"}
>>> print(a)
{'name': 'Jagadeesh', 'city': 'Guntur'}
>>> type(a)
<class 'dict'>
>>> b={5,6,7,8,9,"name"}
>>> type(b)
<class 'set'>
>>> a={"name":"Jagadeesh","mailid":"jagadeesh@gmail.com","mobileno":9878451245}
>>> a.keys()
dict_keys(['name', 'mailid', 'mobileno'])
>>> a.values()
dict_values(['Jagadeesh', 'jagadeesh@gmail.com', 9878451245])
>>> a.items()
dict_items([('name', 'Jagadeesh'), ('mailid', 'jagadeesh@gmail.com'), ('mobileno', 9878451245)])
>>> a={"course":"python","institute":"codegnan"}
>>> a.update({"name":"Jagadeesh"})
>>> a
{'course': 'python', 'institute': 'codegnan', 'name': 'Jagadeesh'}
>>> a.update({"year":2026,"month":"July"})
>>> a
{'course': 'python', 'institute': 'codegnan', 'name': 'Jagadeesh', 'year': 2026, 'month': 'July'}
>>> a={"year":2026,"month":"July"}
>>> a.setdefault("date",2)
2
>>> a
{'year': 2026, 'month': 'July', 'date': 2}
>>> a={"time":12,"hour":1,"min":13}
>>> a
{'time': 12, 'hour': 1, 'min': 13}
a={"college":"vignan","branch":"IT"}
a.get("college")
'vignan'
a.get("branch")
'IT'
a={"hour":12,"min":3,"sec":60}
a.copy()
{'hour': 12, 'min': 3, 'sec': 60}
a.clear()
a
{}
b={}
b.update({"name":"Vinod"})
b
{'name': 'Vinod'}
a={"name":"vinod","course":"vja","age":22}
len(a)
3
#duplicates in dictionary
a={"name":"vinod","course":"vja","name":"vinod"}
print(a)
{'name': 'vinod', 'course': 'vja'}
a={"name":"vinod","course":"vja","name":"vijay"}
print(a)
{'name': 'vijay', 'course': 'vja'}
a={"name1":"vinod","course":"vja","name2":"vijay"}
print(a)
{'name1': 'vinod', 'course': 'vja', 'name2': 'vijay'}
a={"idnos":[10,20,30],"names":["Ajay","Harsha","Sanjay"],"marks":[60,70,80]}
print(a)
{'idnos': [10, 20, 30], 'names': ['Ajay', 'Harsha', 'Sanjay'], 'marks': [60, 70, 80]}
type(a)
<class 'dict'>
a.keys()
dict_keys(['idnos', 'names', 'marks'])
a.values()
dict_values([[10, 20, 30], ['Ajay', 'Harsha', 'Sanjay'], [60, 70, 80]])
a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['Ajay', 'Harsha', 'Sanjay']), ('marks', [60, 70, 80])])
len(a)
3
