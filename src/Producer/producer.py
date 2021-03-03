import boto3
import json
from datetime import datetime
import calendar
import random
import time
import string
from random import randrange

sns_client = boto3.client('sns')
sns_arn = 'SNS_ARN'

my_stream_name = 'stream-demo'
kinesis_client = boto3.client('kinesis', region_name='us-east-1')

eb_client = boto3.client('events')

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def put_to_stream(payload):
    partition_key = 'user-aa-bb'
    print(payload)
    put_response = kinesis_client.put_record(
                        StreamName=my_stream_name,
                        Data=json.dumps(payload),
                        PartitionKey=partition_key)
def put_to_topic(payload):
    response = sns_client.publish(
        TargetArn = sns_arn,
        Message = json.dumps(payload),
        MessageAttributes = {
            'colour': {
                'DataType': 'String',
                'StringValue': payload.get('colour')
        }})
def put_to_eventbridge(payload):
    eb_client.put_events(
        Entries=[
        {
            'Source': 'publisher',
            'DetailType': 'publishevent',
            'Detail': json.dumps(payload),
            'EventBusName': 'my-bus'
        }
        ]
    )
while True:
    colours = ['blue', 'red', 'green', 'all']
    colour = random.choice(colours)
    property_timestamp = calendar.timegm(datetime.utcnow().timetuple())
    payload = {
                'colours': str(colour),
                'somenumber' : randrange(101),
                'message' : {'somestring' : get_random_string(10),
                            'someotherstring' : get_random_string(5)},
                'timestamp': str(property_timestamp),
              }
    put_to_stream(payload)
    put_to_topic(payload)
    put_to_eventbridge(payload)
    # wait for 5 second
    time.sleep(1)

