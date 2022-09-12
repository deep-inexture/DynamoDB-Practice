import boto3


def delete_devices_table(dynamodb=None):
    dynamodb = boto3.resource('dynamodb')
    # specify the table to be deleted
    devices_table = dynamodb.Table('Devices')
    devices_table.delete()


delete_devices_table()
print('Table Deleted')