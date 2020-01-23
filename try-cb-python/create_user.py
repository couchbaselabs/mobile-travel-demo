import requests
import sys
import json
import getpass
import md5

userName="demo"
userPass="password"
md5Pass=md5.new()

if sys.stdin.isatty():
   print "Enter credentials for Travel Demo"
   userName = raw_input("Username: ")
   userPass = getpass.getpass("Password: ")
   md5Pass.update(userPass)
   hashPass=md5Pass.hexdigest()
else:
   userName = sys.stdin.readline().rstrip()
   userPass = sys.stdin.readline().rstrip()

print "Username: [%s], password [%s]" % (userName, hashPass)


headerInfo = {'Content-type': 'application/json', 'Accept': 'application/json'}

appUrl = "http://localhost:8080/api/user/signup"
#appValues = json.dumps({"user" : userName, "password" : userPass})
appValues = json.dumps({"user" : userName, "password" : hashPass})
appUser = requests.post(appUrl, headers=headerInfo, data=appValues)
print "Created user" + appUser.text,appUser.status_code

sgUrl = "http://localhost:4985/travel-sample/_user/"
sgValues = json.dumps({"name" : userName, "password" : userPass})
sgUser = requests.post(sgUrl, headers=headerInfo, data=sgValues)
print "Created user" + str(sgUser.text),str(sgUser.status_code)
