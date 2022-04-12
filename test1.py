from flask import Flask, jsonify, abort
from flask_restful import Resource, Api, reqparse
import pandas
import json
import os
from google.cloud import firestore

#Working towards web application for chat functionality
#TODO formating application screens

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ttaylor-med-api-3285443a6f89.json'

db = firestore.Client()
deviceRef = db.collection(u'devices')


deviceDocs = deviceRef.stream()
devices = {}
deviceIDList = []
i = 0

for device in deviceDocs:
    #print(f'{device.id} => {device.to_dict()}')
    devices[device.id] = device.to_dict()
    deviceIDList.append(device.id)
    print(deviceIDList)
    i = i + 1

#print(device.id)