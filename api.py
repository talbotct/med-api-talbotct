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
        data = pandas.read_csv('Data.csv').to_dict()

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
        data = pandas.read_csv('Data.csv')

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
            data.to_csv('Data.csv', index=False)
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
        data = pandas.read_csv('Data.csv')

        # checks input patient ID if valid change the input values
        if args['patientID'] in list(data['patientID']):
            if(args['name']):
                (data.at[0, 'name']) = (args['name'])
            if(args['hospital']):
                (data.at[0, 'hospital']) = (args['hospital'])
            if(args['temperature']):
                (data.at[0, 'temperature']) = (args['temperature'])
            if(args['systolicBP']):
                (data.at[0, 'systolicBP']) = (args['systolicBP'])
            if(args['diastolicBP']):
                (data.at[0, 'diastolicBP']) = (args['diastolicBP'])
            if(args['pulse']):
                (data.at[0, 'pulse']) = (args['pulse'])
            if(args['oximeter']):
                (data.at[0, 'oximeter']) = (args['oximeter'])
            if(args['weight']):
                (data.at[0, 'weight']) = (args['weight'])
            if(args['glucometer']):
                (data.at[0, 'glucometer']) = (args['glucometer'])

            # creates the updated file
            data.to_csv('Data.csv', index=False)
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
        data = pandas.read_csv('Data.csv')

        if args['patientID'] in list(data['patientID']):
            data = data[data['patientID'] != args['patientID']]

            # appends the new data
            data.to_csv('Data.csv', index=False)
            # creates the updated file
            return {'data': data.to_dict()}, 200
        else:
            return 404


# Creates Patients as a resource in the API
api.add_resource(Patients, '/patients')

# runs api app
if __name__ == '__main__':
    app.run()
