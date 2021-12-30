from typing import Union
from mongoengine import *


def get_pesticide_by_id(db, _id: int) -> Document:
    """
    Function for accessing pesticidesDB, returns the pesticide corresponding to "pesticide_id"
    :param _id: int - an id for a pesticide
    :return: the pesticide's document as a dict
    """
    collection = db.pesticides
    return collection.find_one({"_id": _id})


def get_specific_pesticide_field(db, _id: int, field: str) -> Union[int, str, list]:
    """
    Function for accessing pesticidesDB, returns the value of the given field for the pesticide corresponding to "pesticide_id"
    :param _id: int - an id for a pesticide
    :param field: str - a field in a pesticide document
    :return: a value of a field for a pesticide
    """
    collection = db.pesticides
    return collection.find_one({'_id': _id})[field]
