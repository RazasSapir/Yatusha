from mongoengine import *
from .pesticing_class import PesticingToDB



class Update_and_delete(Document):
	def update_DB(obj, obj_to_change, obj_to_put):
		try:
			PesticingToDB.objects.filter()
		except Exception as e:
			raise ("Invalid update", e)

	def delete_DB(col, client, value_to_delete, mongo_client):
		try:
			db = mongo_client["user_data"]
			db_col = db["col"]

			db_col.delete_one(value_to_replace, value_to_put)
		except Exception as e:
			raise ("Invalid update", e)