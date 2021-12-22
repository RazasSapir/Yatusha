from pymongo import MongoClient
from datetime import datetime
import pymongo


def find_pesticide_by_key(key, value):
    client = MongoClient()
    db = client.pest_test
    collection = db.pest_test_collection

    if key == '_id':
        value = int(value)
    elif key == 'expiration_date':
        value = datetime.strptime(value, "%d/%m/%Y")
    elif key == 'general_public_permission':
        value = value == 'true'

    docs = collection.find({key: value}).sort([('_id', pymongo.ASCENDING)])
    for doc in docs:
        print(doc)

    """
    proofs of concepts:
    
prints only name, manufacturer and designation for pesticides that are for exterminators only, sorted by id in ascending order:
    extra_docs = collection.find({'general_public_permission': False},
                                 {'_id': 0, 'name': 1, 'manufacturer': 1,'designation': 1}).sort([('_id', pymongo.ASCENDING)])
    for doc in extra_docs:
        print(doc)

prints every pesticide that has an id number greater than 500 and its form is either ג'ל or אירוסול.
    extra_extra_docs = collection.find({'_id': {'$gt': 500}, 'form': {'$in': ['אירוסול', "ג'ל"]}})
    for doc in extra_extra_docs:
        print(doc)
"""


def main():
    find_pesticide_by_key(input('Enter key:    ').lower(), input('Enter value:    ').lower())


if __name__ == '__main__':
    main()
