from pymongo import MongoClient
from typing import Union


def get_pesticide_by_id(_id: int) -> dict:
    """
    Function for accessing pesticidesDB, returns the pesticide corresponding to "pesticide_id"
    :param _id: int - an id for a pesticide
    :return: the pesticide's document as a dict
    """
    client = MongoClient()
    db = client.pesticidesDB
    collection = db.pesticides
    return collection.find_one({"_id": _id})


def get_specific_pesticide_field(_id: int, field: str) -> Union[int, str, list]:
    """
    Function for accessing pesticidesDB, returns the value of the given field for the pesticide corresponding to "pesticide_id"
    :param _id: int - an id for a pesticide
    :param field: str - a field in a pesticide document
    :return: a value of a field for a pesticide
    """
    client = MongoClient()
    db = client.pesticidesDB
    collection = db.pesticides
    return collection.find_one({'_id': _id})[field]
