import boto3
from flask import Flask, jsonify, request
app = Flask(__name__)
dynamodb = boto3.client('dynamodb', region_name = 'us-east-1')    

@app.route('/', methods = ['POST'])
def pushToDynamodb():
    request_data = request.get_json()
    dynamodb.put_item(TableName='final',
    Item={'first-name':{'S': request_data['first_name']},
    'Company': {'S': request_data['company']} ,
    'address1': {'S': request_data['address1']} ,
    'address2': {'S': request_data['address2']} ,
    'city': {'S': request_data['city']} ,
    'state': {'S': request_data['state']} ,
    'zip': {'S': request_data['zip']},
    'email': {'S': request_data['email']} ,
    'phone': {'S': request_data['phone']} ,
    'budget': {'S': request_data['budget']} ,
    'message': {'S': request_data['message']}  } )
    return jsonify(request_data)