import json

studentsList = []
print("Started Reading JSON file which contains multiple JSON document")
with open('/Users/user/Desktop/APIAutomation/GetRequest/postData.txt') as f:
    for jsonObj in f:
        studentDict = json.loads(jsonObj)
        studentsList.append(studentDict)

print("Printing each JSON Decoded Object")
for student in studentsList:
    print(student["id"], student["name"], student["class"], student["email"])
