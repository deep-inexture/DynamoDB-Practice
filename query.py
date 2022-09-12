import boto3
from boto3.dynamodb.conditions import Key


def query_devices(device_id, dynamodb=None):
    dynamodb = boto3.resource('dynamodb')
    # Specify the table to query
    device_tables = dynamodb.Table('Devices')
    response = device_tables.query(
        KeyConditionExpression=Key('device_id').eq(device_id)
    )
    return response['Items']


query_id = "10001"
print(f"Device Data from Device ID: {query_id}")
devices_data = query_devices(query_id)
# Print the items returned
for device_data in devices_data:
    print(device_data['device_id'], ":", device_data['datacount'])
