# TODO: put in a different module

from mongoengine import *
import csv
from datetime import datetime


# TODO: Remove this connect
connect('pest_class')
# TODO: Add PesticidesDB_CSV_PATH to Server Settings
PATH = r'..\assets\pesticides.csv'


class Pesticide(Document):
    name = StringField(required=True)
    manufacturer = StringField(required=True)
    _id = IntField(required=True, primary_key=True)
    form = StringField(required=True)
    expiration_date = DateField(required=True)
    active_ingredients = ListField(required=True)
    designation = StringField(required=True)
    general_public_permission = BooleanField(required=True)
    meta = {'collection': 'plz_work'}

    # TODO: Add validation checks
    def __init__(self, row):
        super().__init__()
        self.name = row[0]
        self.manufacturer = row[1]
        self._id = int(row[2])
        self.form = row[3]
        self.expiration_date = datetime.strptime(row[4], "%d/%m/%Y")
        self.active_ingredients = row[5].split(", ")
        self.designation = row[6]
        self.general_public_permission = row[7] == 'הקהל הרחב'


def csv_to_mondo(path):
    file = open(path, 'r', encoding='utf8')
    csv_reader = csv.reader(file)
    header = next(csv_reader)

    for i in csv_reader:
        pesticide = Pesticide(i)
        pesticide.save()


# TODO: this command and add it to server_config function in Server/Server.py
csv_to_mondo(PATH)
