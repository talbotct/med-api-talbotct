from flask import Flask, jsonify, abort
from flask_restful import Resource, Api, reqparse
import os
from google.cloud import firestore

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ttaylor-med-api-3285443a6f89.json'

db = firestore.Client()
userRef = db.collection(u'users')

userDocs = userRef.stream()
users = {}
i = 0

for user in userDocs:
    #print(f'{device.id} => {device.to_dict()}')
    users[user.id] = user.to_dict()
    i = i + 1

userPostArgs = reqparse.RequestParser()
userPostArgs.add_argument("name", type = str, required = True)
userPostArgs.add_argument("role", type = str, required = True)
userPostArgs.add_argument("admin", type = str, required = True)
userPostArgs.add_argument("hospital", type = str, required = True)
userPostArgs.add_argument("temperature", type = str)
userPostArgs.add_argument("pulse", type = str)
userPostArgs.add_argument("doctors", type = str)
userPostArgs.add_argument("nurses", type = str)
userPostArgs.add_argument("patients", type = str)

userPutArgs = reqparse.RequestParser()
userPutArgs.add_argument("name", type = str)
userPutArgs.add_argument("role", type = str)
userPutArgs.add_argument("admin", type = str)
userPutArgs.add_argument("hospital", type = str)
userPutArgs.add_argument("temperature", type = str)
userPutArgs.add_argument("pulse", type = str)
userPutArgs.add_argument("doctors", type = str)
userPutArgs.add_argument("nurses", type = str)
userPutArgs.add_argument("patients", type = str)

class userList(Resource):
    def get(self):
        return users

    #POST
    def post(self):
        args = userPostArgs.parse_args()

        users = {
                "name": args["name"],
                "role": args["role"],
                "admin": args["admin"],
                "hospital": args["hospital"],
                "temperature": args["temperature"],
                "pulse": args["pulse"],
                "doctors": args["doctors"],
                "nurses": args["nurses"],
                "patients": args["patients"]
            }
            
        #POSTS to google firestore database
        holder = userRef.add(users)        
    
        return users

class user(Resource):
    #GET
    def get(self, userID):
        return users[userID]

    #PUT
    def put(self, userID):
        args = userPutArgs.parse_args()

        if userID not in users:
            abort(404, "UserID does not exist")

        else:
            if(args['name']):
                users[userID]['name'] = (args['name'])
                holder = userRef.document(userID)
                holder.update({u'name': args['name']})
            if(args['role']):
                users[userID]['role'] = (args['role'])
                holder = userRef.document(userID)
                holder.update({u'role': args['role']})
            if(args['admin']):
                users[userID]['admin'] = (args['admin'])
                holder = userRef.document(userID)
                holder.update({u'admin': args['admin']})
            if(args['hospital']):
                users[userID]['hospital'] = (args['hospital'])
                holder = userRef.document(userID)
                holder.update({u'hospital': args['hospital']})
            if(args['temperature']):
                users[userID]['temperature'] = (args['temperature'])
                holder = userRef.document(userID)
                holder.update({u'temperature': args['temperature']})
            if(args['pulse']):
                users[userID]['pulse'] = (args['pulse'])
                holder = userRef.document(userID)
                holder.update({u'pulse': args['pulse']})
            if(args['doctors']):
                users[userID]['doctors'] = (args['doctors'])
                holder = userRef.document(userID)
                holder.update({u'doctors': args['doctors']})
            if(args['nurses']):
                users[userID]['nurses'] = (args['nurses'])
                holder = userRef.document(userID)
                holder.update({u'nurses': args['nurses']})
            if(args['patients']):
                users[userID]['patients'] = (args['patients'])
                holder = userRef.document(userID)
                holder.update({u'patients': args['patients']})

        return users[userID]

    #DELETE
    def delete(self, userID):
        if userID not in users:
            abort(404, "UserID does not exist")
    
        else:
            holder = userRef.document(userID).delete()

            del users[userID]
        
        return users

#if __name__ == '__main__':
    #app.run()