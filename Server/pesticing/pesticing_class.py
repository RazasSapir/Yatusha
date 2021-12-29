from mongoengine import *
from datetime import datetime

connect(host="127.0.0.1", port=27017)


now = datetime.utcnow()


class PesticingToDB(Document):
    name = StringField(min_length=3)  # at least 2 chars and one space
    license_type = IntField(min_value=0, max_value=4)
    license_number = StringField()
    location = ListField()  # the location, should be PointField in progress...
    time = DateTimeField(default=now.strftime("%d/%m/%Y %H:%M:%S"))  # the time of the Pesticing form
    place_type = StringField(
        choices=("Private Place", "Public Space", "Nature"))  # touple of all place types that can be
    pest_type = StringField()
    pesticides_ID = StringField()  # from 1 (min length) to 1000 (mac length)
    additional_information = StringField()
