from cloudant.client import CouchDB
import json

USERNAME = "admin"
PASSWORD = "ufologie"

client = CouchDB(USERNAME, PASSWORD, url='http://127.0.0.1:5984', connect=True)
ufo_db = client.create_database('ufo')
ufo_db = client['ufo']

print("state;ufo_report_count")
for row in ufo_db.get_view_result('report_state_count', 'city_state_count', include_docs=False, reduce=True, group=True):
    json_data = ufo_db.get_list_function_result('report_state_count', 'add_value', 'city_report_count', include_docs=False, reduce=True, group=True, keys=row['value'])
    total_count = json.loads(json_data)['total_count']

    print("{};{}".format(row['key'], total_count))
