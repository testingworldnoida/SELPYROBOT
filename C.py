import json
data= open('E:/Data1.json','r')
req=data.read()
json_request=json.loads(req)
json_request['first_name']="testing"
print(json_request)
