import json
f= open("E:\Data1.json",'r')
d= f.read()
json1= json.loads(d)
print(json1)