import os
import json
import datetime
import asyncio


def currentCorona():
    with open('./data/corona.json', encoding="utf-8") as json_data_file:
        currentCorona = json.load(json_data_file)
    return currentCorona


def newCorona(coronaJson):
    ts = datetime.datetime.now().timestamp()

    with open('./data/corona.json', encoding="utf-8") as json_data_file:
        currentCoronaJSON = json.load(json_data_file)

    lastTimestamp = currentCoronaJSON['timestamp']
    coronaObj = json.loads(coronaJson)
    coronaObj['name'] = getNewCoronaName(coronaObj['name'])
    # назначение полученных данных
    currentCoronaJSON['name'] = coronaObj['name']
    currentCoronaJSON['ownerId'] = coronaObj['ownerId']
    currentCoronaJSON['timestamp'] = ts

    currentCoronaJSON['old']['name'] = deleteCoronaName(
        currentCoronaJSON['old']['name'])

    file_object = open('./data/corona.json', 'w')
    json.dump(currentCoronaJSON, file_object)

    now = datetime.datetime.now().timestamp()
    duration = now - lastTimestamp

    currentCoronaJSON['string'] = "korona uje {}".format(duration)

    return currentCoronaJSON


def deleteCoronaName(name):
    newName = name.replace("♔", "")
    return newName


def getNewCoronaName(name):
    newName = "♔ " + name
    return newName
