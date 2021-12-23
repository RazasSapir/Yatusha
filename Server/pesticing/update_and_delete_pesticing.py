from mongoengine import *
from .pesticing_class import PesticingToDB

connect(host = "127.0.0.1", port = 27017)

class Update_and_delete():
	@staticmethod
	def update_DB(obj:PesticingToDB, obj_to_change:str, obj_to_put):
		try:
			objects = {"additional_information" : obj.additional_information, "license_number" : obj.license_number, \
					   "name" : obj.name, "license_type" : obj.license_type, "pest_type" : obj.pest_type, \
					   "pesticides_ID" : obj.pesticides_ID, "place_type" : obj.place_type}
			objects[obj_to_change] = obj_to_put
			obj.save()
		except Exception as e:
			raise ("Invalid update", e)

	'''def delete_DB(col, client, value_to_delete, mongo_client):
		try:
			db = mongo_client["user_data"]
			db_col = db["col"]

			db_col.delete_one(value_to_replace, value_to_put)
		except Exception as e:
			raise ("Invalid update", e)'''