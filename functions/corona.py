import os
import json
import datetime


def currentCorona():
    with open('./data/corona.json', encoding="utf-8") as json_data_file:
        currentCorona = json.load(json_data_file)
    return currentCorona


def newCorona(coronaJson):
    ts = datetime.datetime.now().timestamp()
    with open('./data/corona.json', encoding="utf-8") as json_data_file:
        currentCoronaJSON = json.load(json_data_file)
    then = currentCoronaJSON['timestamp']
    coronaObj = json.loads(coronaJson)
    currentCoronaJSON['name'] = coronaObj['name']
    currentCoronaJSON['ownerId'] = coronaObj['ownerId']
    currentCoronaJSON['timestamp'] = ts
    file_object = open('./data/corona.json', 'w')
    json.dump(currentCoronaJSON, file_object)

    now = datetime.datetime.now().timestamp()
    duration = now - then

    currentCoronaJSON['string'] = "korona uje {}".format(duration)

    return currentCoronaJSON
