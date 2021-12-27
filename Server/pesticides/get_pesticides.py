from pymongo import MongoClient


def get_pesticide_by_id(_id):
    """
    :param _id: an id for a pesticide
    :return: the pesticide's document
    """
    client = MongoClient()
    db = client.pesticidesDB
    collection = db.pesticides
    return collection.find_one({"_id": _id})


def get_specific_pesticide_field(_id, field):
    """
    :param _id: an id for a pesticide
    :param field: a field in a pesticide document
    :return: the value of that field for the pesticide corresponding to that id
    """
    client = MongoClient()
    db = client.pesticidesDB
    collection = db.pesticides
    return collection.find_one({'_id': _id})[field]
