import requests
import json

userName="user1"
userPass="password"

headerInfo = {'Content-type': 'application/json', 'Accept': 'application/json'}

appUrl = "http://localhost:8080/api/user/signup"
appValues = json.dumps({"user" : userName, "password" : userPass})
appUser = requests.post(appUrl, headers=headerInfo, data=appValues)
print "Created user" + appUser.text,appUser.status_code

sgUrl = "http://localhost:4985/travel-sample/_user/"
sgValues = json.dumps({"name" : userName, "password" : userPass})
sgUser = requests.post(sgUrl, headers=headerInfo, data=sgValues)
print "Created user" + sgUser.text,sgUser.status_code
