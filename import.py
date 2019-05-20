from cloudant.client import CouchDB
import csv

USERNAME = "admin"
PASSWORD = "ufologie"

client = CouchDB(USERNAME, PASSWORD, url='http://127.0.0.1:5984', connect=True)
ufo_db = client.create_database('ufo')
ufo_db = client['ufo']


def add_row_to_couchdb(row):
    report = {
      "type": "report",
      "Duration": row[6],
      "Description": row[7],
      "Occured": row[1],
      "Shape": row[5],
      "city_name": row[3]
    }

    city = {
        "type": "city",
        "_id": row[3],
        "name": row[3],
        "state_name": row[4]
    }

    state = {
        "type": "state",
        "_id": row[4],
        "name": row[4]
    }

    if row[4] and row[3]:
        ufo_db.create_document(state)
        ufo_db.create_document(city)
        ufo_db.create_document(report)


def read_csv():
    csv.register_dialect('csvstyle', delimiter=';')
    with open('ufo.csv', 'r', encoding="latin-1") as csvFile:
        reader = csv.reader(csvFile, dialect="csvstyle")
        for idx, row in enumerate(reader):
            print(idx)
            add_row_to_couchdb(row)


if __name__ == "__main__":
    read_csv()


# Disconnect from the server
client.disconnect()
