import time

print('Table Creation in Progress...')
import create_table
print('Table Created Successfully')
time.sleep(5)
print('Json Data Insertion in Progress...')
import load_data
print('Json Data Inserted Successfully')
time.sleep(2)
print('Individual Data Insertion in Process...')
import create_item
print('Individual Data Inserted Successfully')
time.sleep(2)
print('Fetching Items from Database...')
import read_item
print('Data Fetched Successfully')
time.sleep(2)
print('Data Updation in Progress...')
import update_item
print('Data Updation Completed')
time.sleep(2)
print('Individual Item Deletion in Progress...')
import delete_item
print('Item Deleted Successfully')
time.sleep(2)
print('Performing query on all items...')
import query
print('Querying Completed')
time.sleep(2)
print('Performing scanning on all Items')
import scan
print('Scanning Completed')
time.sleep(2)
print('Table Deletion in Progress...')
import delete_table
print('Table Deleted Successfully')