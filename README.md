# EC 530 Project 2 Medical API

This is an in progress API meant to be a tool for managing a medical database.

Currently supports simple REST API actions: Post, Get, Put, Delete

# Usage
User can run "api.py" which will launch the Flask app on the localhost.  Then can use API using either a web brower or a tool such as Postman https://www.postman.com/downloads/.

Current data fields for medical records: userId,name,hospital,temperature,systolicBP,diastolicBP,pulse,oximeter,weight,glucometer

Currently only supports usage on the localhost and editing of a local .csv file.  Plan on deploying on free AWS services for hosting.

# Resources
API Status Codes
https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

Basic API Stucture
https://flask-restful.readthedocs.io/en/latest/quickstart.html
