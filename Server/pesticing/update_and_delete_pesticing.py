from bson.objectid import ObjectId
from mongoengine import *
from pymongo import MongoClient

# TODO: Remove and use mongoengine
connect(host="127.0.0.1", port=27017)
client = MongoClient("127.0.0.1", 27017)


class Update_and_delete():
    @staticmethod
    def update_DB(obj_to_change: str, obj_to_put, obj_id: str):
        # try:
        db = client.database
        collection = db.collection
        query_to_update = collection.find_one({"_id": ObjectId(obj_id)})
        objects = {"additional_information": query_to_update.additional_information,
                   "license_number": query_to_update.license_number,
                   "name": query_to_update.name,
                   "license_type": query_to_update.license_type,
                   "pest_type": query_to_update.pest_type,
                   "pesticides_ID": query_to_update.pesticides_ID,
                   "place_type": query_to_update.place_type}
        query_to_update.update_one(objects[obj_to_change], obj_to_put)

    # except Exception as e:
    # raise ("Invalid update", e)

    '''def delete_DB(col, client, value_to_delete, mongo_client):
        try:
            db = mongo_client["user_data"]
            db_col = db["col"]

            db_col.delete_one(value_to_delete)
        except Exception as e:
            raise ("Invalid update", e)'''
