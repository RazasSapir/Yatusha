from datetime import datetime
from typing import Union

from bson.objectid import ObjectId
from mongoengine import *


class PesticidingAction(Document):
    name = StringField(min_length=3)  # at least 2 chars and one space
    license_type = IntField(min_value=0, max_value=4)
    license_number = StringField()
    location = ListField()  # the location, should be PointField in progress...
    time = DateTimeField(default=datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S"))  # the time of the Pesticing form
    place_type = StringField(
        choices=("Private Place", "Public Space", "Nature"))  # touple of all place types that can be
    pest_type = StringField()
    pesticides_ID = StringField()  # from 1 (min length) to 1000 (mac length)
    additional_information = StringField()
    meta = {'collection': 'PestingActions'}


def update_db(db, obj_to_change: str, obj_to_put: Union[str, int], obj_id: str):
    """
    function to update the specific query in our database
    :param obj_to_change: the object we want to change
    :param obj_to_put: the object we want to put
    :param obj_id: the id of the query
    :return: the updated query
    """
    try:
        collection = db.PestingActions  # getting the collection
        query_to_update = collection.find_one({'_id': ObjectId(obj_id)})  # find the query to update and put
        # it inside dictionary
        query_to_update[obj_to_change] = obj_to_put  # put the object we want to put inside the database
        collection.replace_one(collection.find_one({'_id': ObjectId(obj_id)}), query_to_update)  # res is
        # only for debugging not necessary to pus the function in a variable
        return query_to_update  # returns the updated query

    except ValueError as e:  # check if the update is valid
        raise ("Invalid update", e)  # if not valid raise an error


def delete_db(db, obj_id: str):
    """
    function to delete query from the database
    :param obj_id: the id of the query to delete
    :return: the query we deleted
    """
    try:
        collection = db.PestingActions
        query_to_delete = collection.find_one({'_id': ObjectId(obj_id)})
        collection.remove({"_id": ObjectId(obj_id)}, {'justOne': True})

        return query_to_delete

    except ValueError as e:
        raise ("something went wrong", e)
