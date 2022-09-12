import boto3        # Import Boto3

"""
We are going to create a table called Devices using the method create_table. 
The table has attributes device_id as the partition key and data-count as the sort key. 
"""


def create_devices_table(dynamodb=None):
    dynamodb = boto3.resource('dynamodb')
    # Table definition
    table = dynamodb.create_table(
        TableName='Devices',
        KeySchema=[
            {
                'AttributeName': 'device_id',
                'KeyType': 'HASH'                   # Partition Key
            },
            {
                'AttributeName': 'datacount',
                'KeyType': 'RANGE'                   # Sort Key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'device_id',
                # AttributeType defines the data type. 'S' is string type and 'N' is number type
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'datacount',
                'AttributeType': 'N'
            },
        ],
        ProvisionedThroughput={
            # ReadCapacityUnits set to 10 strongly consistent reads per second
            'ReadCapacityUnits': 10,
            # WriteCapacityUnits set to 10 writes per second
            'WriteCapacityUnits': 10
        }
    )
    return table


device_table = create_devices_table()
# Print Table Status
print(f"Status: {device_table.table_status}")
