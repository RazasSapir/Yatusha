import csv
from datetime import datetime

from mongoengine import *


class Pesticide(Document):
    name = StringField(required=True)
    manufacturer = StringField(required=True)
    _id = IntField(required=True, primary_key=True)
    form = StringField(required=True)
    expiration_date = DateField(required=True)
    active_ingredients = ListField(required=True)
    designation = StringField(required=True)
    general_public_permission = BooleanField(required=True)
    meta = {'collection': 'pesticides'}

    def __init__(self, row):
        super().__init__()
        self._id = int(row[0])
        self.name = row[1]
        self.expiration_date = datetime.strptime(row[5], "%d/%m/%Y")
        self.manufacturer = row[2]
        self.form = row[4]
        self.active_ingredients = row[6].split(", ")
        self.general_public_permission = row[8] == 'הקהל הרחב'
        self.designation = row[7]


def csv_to_mondo(db, path: str) -> None:
    """
    Function for saving pesticides.csv to mongoDB
    :param: db - the database
    :param: path: str - the path for the csv file
    :return: nada
    """
    # opens pesticides.csv:
    file = open(path, 'r', encoding='utf8')
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # the first row in pesticides.csv is only titles, so it is skipped, it is irrelevant

    # saves every row in pesticides.csv as a document in the DB by turning them into Pesticide objects
    for i in csv_reader:
        pesticide = Pesticide(i)
        pesticide.save()


# csv_to_mondo(PATH)
