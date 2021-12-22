import csv
from datetime import datetime
from pymongo import MongoClient

PATH = r'C:\Users\tomer\PycharmProjects\Yatusha\assets\pesticides.csv'


def create_dict(row):
    return {'_id': int(row[2]),
            'name': row[0],
            'manufacturer': row[1],
            'form': row[3],
            'expiration_date': datetime.strptime(row[4], "%d/%m/%Y"),
            'active_ingredients': row[5].split(", "),
            'designation': row[6],
            'general_public_permission': row[7] == 'הקהל הרחב'
            }


def csv_to_mondo(path):
    client = MongoClient()
    db = client.pest_test
    collection = db.pest_test_collection

    file = open(path, 'r', encoding='utf8')
    csv_reader = csv.reader(file)
    header = next(csv_reader)

    for i in csv_reader:
        pesticide = create_dict(i)
        collection.insert_one(pesticide)


def main():
    csv_to_mondo(PATH)


if __name__ == '__main__':
    main()