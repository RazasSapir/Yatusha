from mongoengine import *
from pymongo import *
from datetime import datetime

now = datetime.now()

class PesticingToDB(Document):
	name = StringField(min_length = 3)# at least 2 chars and one space
	license_type = IntField(min_value = 0, max_value = 4)
	license_number = StringField()
	location = GeoJSON() # the location
	time = now.strftime("%d/%m/%Y %H:%M:%S") # the time of the Pesticing form
	place_type = StringField() # touple of all place types that can be 
	pest_type = StringField()
	pesticides_ID = StringField(1, 1000) # from 1 (min length) to 1000 (mac length)
	additional_information = StringField() 

	def __init__(self, name, license_type, location, place_type, pest_type, pesticides_ID, additional_information):
	 	self.name = name
	 	self.license_type = license_type
	 	self.location = location
	 	if place_type in ("Private Place", "Public Space", "Nature"):
	 		self.place_type = place_type

	 	else:
	 		raise ValueError("Invalid value")

	 	self.pest_type = pest_type
	 	self.pesticides_ID = pesticides_ID
	 	self.additional_information = additional_information
	
	def to_dict():
		return {'name' : self.name, 'license_type' : str(self.license_type), \
		'location' : str(self.location), 'place_type' : self.place_type, \
		'pest_type' : self.pest_type, 'pesticides_ID' : self.pesticides_ID, \
		'additional_information' : self.additional_information}