import json

FILENAME = "uuid-participants.json"
with open(FILENAME) as fp:
    data = json.load(fp)

while True:
    pid = input("Enter the Unique ID (x to exit)> ")
    if pid.lower() == "x":
        break
    if pid in data.keys():
        if data[pid] != "":
            print("ID Already taken! Please check again!")
            continue
        name = ""
        while name == "":
            name = input("Participant name>")
        data[pid] = name
    else:
        print("Incorrect ID! Please check again!")

with open(FILENAME, "w") as wfp:
    json.dump(data, wfp)