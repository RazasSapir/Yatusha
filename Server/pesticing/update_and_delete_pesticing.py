import collections

from mongoengine import *
from .pesticing_class import PesticingToDB
from bson.objectid import ObjectId
from pymongo import MongoClient

disconnect()
connect(host = "127.0.0.1", port = 27017)
client = MongoClient("127.0.0.1", 27017)

class Update_and_delete(Document):
	@staticmethod
	def update_DB(obj_to_change:str, obj_to_put, obj_id:str):
		'''
		function to update the specific query in our database
		:param obj_to_change: the object we want to change
		:param obj_to_put: the object we want to put
		:param obj_id: the id of the query
		:return: the updated query
		'''
		try:
			db = client.test # getting the database
			collection = db.pesticing_to_d_b # getting the collection
			query_to_update = collection.find_one({'_id': ObjectId(obj_id)}) # find the query to update and put
			# it inside dictionary
			query_to_update[obj_to_change] = obj_to_put # put the object we want to put inside the database
			res = collection.replace_one(collection.find_one({'_id': ObjectId(obj_id)}), query_to_update) # res is
			# only for debugging not necessary to pus the function in a variable
			return query_to_update # returns the updated query


		except ValueError as e: # check if the update is valid
			raise ("Invalid update", e) # if not valid raise an error

	@staticmethod
	def delete_DB(obj_id:str):
		try:
			db = client.test
			collection = db.pesticing_to_d_b
			query_to_delete = collection.find_one({'_id': ObjectId(obj_id)})
			collection.remove({"_id": ObjectId(obj_id)}, {'justOne': True})

			return query_to_delete

		except ValueError as e:
			raise ("something went wrong", e)