from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas

# setting up API base
app = Flask(__name__)
api = Api(app)

# Holds patient information and medical statistics
# patientID controls all functions by selecting which patient to manipulate
class Patients(Resource):

    # GET to see patient data
    def get(self):
        # reads data in data .csv file
        data = pandas.read_csv('Patients.csv').to_dict()

        # 200 is code for all good
        return {'data': data}, 200

    # POST to create new patient data
    def post(self):

        # use reqparse for data validation
        parser = reqparse.RequestParser()
        # add required arguments to be parsed
        parser.add_argument('patientID', required=True)
        parser.add_argument('name')
        parser.add_argument('hospital')
        parser.add_argument('temperature')
        parser.add_argument('systolicBP')
        parser.add_argument('diastolicBP')
        parser.add_argument('pulse')
        parser.add_argument('oximeter')
        parser.add_argument('weight')
        parser.add_argument('glucometer')

        args = parser.parse_args(strict=True)
        # open .csv
        data = pandas.read_csv('Patients.csv')

        # if patientID already in database, refuse
        if args['patientID'] in list(data['patientID']):
            return 400

        else:
            # set values given by post request
            postedData = pandas.DataFrame({
                'patientID': args['patientID'],
                'name': args['name'],
                'hospital': args['hospital'],
                'temperature': args['temperature'],
                'systolicBP': args['systolicBP'],
                'diastolicBP': args['diastolicBP'],
                'pulse': args['pulse'],
                'oximeter': args['oximeter'],
                'weight': args['weight'],
                'glucometer': args['glucometer']

            }, index=[0])

            # appends the new data
            # look at warning pandas.concat
            data = data.append(postedData, ignore_index=True)
            # creates the updated file
            data.to_csv('Patients.csv', index=False)
            return {'data': data.to_dict()}, 201

    # PUT to update fields
    def put(self):
        # use reqparse for data validation
        parser = reqparse.RequestParser()

        parser.add_argument('patientID', required=True)
        parser.add_argument('name')
        parser.add_argument('hospital')
        parser.add_argument('temperature')
        parser.add_argument('systolicBP')
        parser.add_argument('diastolicBP')
        parser.add_argument('pulse')
        parser.add_argument('oximeter')
        parser.add_argument('weight')
        parser.add_argument('glucometer')

        args = parser.parse_args(strict=True)
        data = pandas.read_csv('Patients.csv')

        # checks input patient ID if valid change the input values
        if int(args['patientID']) in list(data['patientID']):

            # get patientID row
            rowID = (list(data['patientID'])).index(int(args['patientID']))

            # set value if new value is input
            if(args['name']):
                (data.at[rowID, 'name']) = (args['name'])
            if(args['hospital']):
                (data.at[rowID, 'hospital']) = (args['hospital'])
            if(args['temperature']):
                (data.at[rowID, 'temperature']) = int(args['temperature'])
            if(args['systolicBP']):
                (data.at[rowID, 'systolicBP']) = int(args['systolicBP'])
            if(args['diastolicBP']):
                (data.at[rowID, 'diastolicBP']) = int(args['diastolicBP'])
            if(args['pulse']):
                (data.at[rowID, 'pulse']) = int(args['pulse'])
            if(args['oximeter']):
                (data.at[rowID, 'oximeter']) = int(args['oximeter'])
            if(args['weight']):
                (data.at[rowID, 'weight']) = int(args['weight'])
            if(args['glucometer']):
                (data.at[rowID, 'glucometer']) = int(args['glucometer'])

            # creates the updated file
            data.to_csv('Patients.csv', index=False)
            return {'data': data.to_dict()}, 201

        # if patientID not in database, refuse
        else:
            return 404

    # DELETE to delete patients by patientID
    def delete(self):
        # same setup to parse requested data
        parser = reqparse.RequestParser()

        parser.add_argument('patientID', required=True)

        args = parser.parse_args(strict=True)
        data = pandas.read_csv('Patients.csv')

        if args['patientID'] in list(data['patientID']):
            data = data[data['patientID'] != args['patientID']]

            # appends the new data
            data.to_csv('Patients.csv', index=False)
            # creates the updated file
            return {'data': data.to_dict()}, 200
        else:
            return 404




class Devices(Resource):

    # GET
    def get(self):
        # reads data in data .csv file
        data = pandas.read_csv('Devices.csv').to_dict()

        # 200 is code for all good
        return {'data': data}, 200

    # POST to create new patient data
    def post(self):

        # use reqparse for data validation
        parser = reqparse.RequestParser()
        # add required arguments to be parsed
        parser.add_argument('deviceID', required=True)
        parser.add_argument('deviceName')
        parser.add_argument('deviceType')
        parser.add_argument('manufacturer')

        args = parser.parse_args(strict=True)
        # open .csv
        data = pandas.read_csv('Devices.csv')

        # if patientID already in database, refuse
        if args['deviceID'] in list(data['deviceID']):
            return 400

        else:
            # set values given by post request
            postedData = pandas.DataFrame({
                'deviceID': args['deviceID'],
                'deviceName': args['deviceName'],
                'deviceType': args['deviceType'],
                'manufacturer': args['manufacturer']

            }, index=[0])

            # appends the new data
            # look at warning pandas.concat
            data = data.append(postedData, ignore_index=True)
            # creates the updated file
            data.to_csv('Devices.csv', index=False)
            return {'data': data.to_dict()}, 201

    # PUT to update fields
    def put(self):
        # use reqparse for data validation
        parser = reqparse.RequestParser()

        parser.add_argument('deviceID', required=True)
        parser.add_argument('deviceName')
        parser.add_argument('deviceType')
        parser.add_argument('manufacturer')

        args = parser.parse_args(strict=True)
        data = pandas.read_csv('Devices.csv')

        # checks input patient ID if valid change the input values
        if int(args['deviceID']) in list(data['deviceID']):

            rowID = (list(data['deviceID'])).index(int(args['deviceID']))

            if(args['deviceName']):
                (data.at[rowID, 'deviceName']) = (args['deviceName'])
            if(args['deviceType']):
                (data.at[rowID, 'deviceType']) = (args['deviceType'])
            if(args['manufacturer']):
                (data.at[rowID, 'manufacturer']) = (args['manufacturer'])

            # creates the updated file
            data.to_csv('Devices.csv', index=False)
            return {'data': data.to_dict()}, 201

        # if patientID not in database, refuse
        else:
            return 404

    # DELETE to delete patients by patientID
    def delete(self):
        # same setup to parse requested data
        parser = reqparse.RequestParser()

        parser.add_argument('deviceID', required=True)

        args = parser.parse_args(strict=True)
        data = pandas.read_csv('Devices.csv')

        if args['deviceID'] in list(data['deviceID']):
            data = data[data['deviceID'] != args['deviceID']]

            # appends the new data
            data.to_csv('Devices.csv', index=False)
            # creates the updated file
            return {'data': data.to_dict()}, 200
        else:
            return 404



class MedicalProfs(Resource):

    # GET
    def get(self):
        # reads data in data .csv file
        data = pandas.read_csv('MedicalProfs.csv').to_dict()

        # 200 is code for all good
        return {'data': data}, 200

    # POST to create new patient data
    def post(self):

        # use reqparse for data validation
        parser = reqparse.RequestParser()
        # add required arguments to be parsed
        parser.add_argument('jobID', required=True)
        parser.add_argument('name')
        parser.add_argument('jobTitle')
        parser.add_argument('hospital')
        parser.add_argument('specialty')
        parser.add_argument('ward')
        parser.add_argument('admin')

        args = parser.parse_args(strict=True)
        # open .csv
        data = pandas.read_csv('MedicalProfs.csv')

        # if patientID already in database, refuse
        if args['jobID'] in list(data['jobID']):
            return 400

        else:
            # set values given by post request
            postedData = pandas.DataFrame({
                'deviceID': args['jobID'],
                'deviceName': args['name'],
                'deviceType': args['jobTitle'],
                'manufacturer': args['hospital'],
                'deviceID': args['specialty'],
                'deviceName': args['ward'],
                'deviceType': args['admin']

            }, index=[0])

            # appends the new data
            # look at warning pandas.concat
            data = data.append(postedData, ignore_index=True)
            # creates the updated file
            data.to_csv('MedicalProfs.csv', index=False)
            return {'data': data.to_dict()}, 201

    # PUT to update fields
    def put(self):
        # use reqparse for data validation
        parser = reqparse.RequestParser()

        parser.add_argument('jobID', required=True)
        parser.add_argument('name')
        parser.add_argument('jobTitle')
        parser.add_argument('hospital')
        parser.add_argument('specialty')
        parser.add_argument('ward')
        parser.add_argument('admin')

        args = parser.parse_args(strict=True)
        data = pandas.read_csv('MedicalProfs.csv')

        # checks input patient ID if valid change the input values
        if int(args['jobID']) in list(data['jobID']):

            rowID = (list(data['jobID'])).index(int(args['jobID']))

            if(args['name']):
                (data.at[rowID, 'name']) = (args['name'])
            if(args['deviceType']):
                (data.at[rowID, 'deviceType']) = (args['deviceType'])
            if(args['jobTitle']):
                (data.at[rowID, 'jobTitle']) = (args['jobTitle'])
            if(args['hospital']):
                (data.at[rowID, 'hospital']) = (args['hospital'])
            if(args['specialty']):
                (data.at[rowID, 'specialty']) = (args['specialty'])
            if(args['ward']):
                (data.at[rowID, 'ward']) = (args['ward'])
            if(args['admin']):
                (data.at[rowID, 'admin']) = (args['admin'])

            # creates the updated file
            data.to_csv('MedicalProfs.csv', index=False)
            return {'data': data.to_dict()}, 201

        # if patientID not in database, refuse
        else:
            return 404

    # DELETE to delete patients by patientID
    def delete(self):
        # same setup to parse requested data
        parser = reqparse.RequestParser()

        parser.add_argument('jobID', required=True)

        args = parser.parse_args(strict=True)
        data = pandas.read_csv('MedicalProfs.csv')

        if args['jobID'] in list(data['jobID']):
            data = data[data['jobID'] != args['jobID']]

            # appends the new data
            data.to_csv('MedicalProfs.csv', index=False)
            # creates the updated file
            return {'data': data.to_dict()}, 200
        else:
            return 404

# Creates Patients as a resource in the API
api.add_resource(Patients, '/patients')
api.add_resource(Devices, '/devices')
api.add_resource(MedicalProfs, '/medicalProfs')

# runs api app
if __name__ == '__main__':
    app.run()
