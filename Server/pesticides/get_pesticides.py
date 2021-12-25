from pymongo import MongoClient
from datetime import datetime
import pymongo


def get_pesticide_by_id(id):
    client = MongoClient()
    db = client.pesticidesDB
    collection = db.pesticides
    return collection.find_one({"_id": id})


def get_specific_pesticide_field(id, field):
    client = MongoClient()
    db = client.pesticidesDB
    collection = db.pesticides
    return collection.find_one({'_id': id})[field]