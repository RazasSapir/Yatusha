import mongoengine
import bcrypt
import base64
import hashlib
import flask


#  create login class
class LoginInformation(mongoengine.Document):
    username_or_email = mongoengine.StringField(required=True)
    password = mongoengine.StringField(required=True)
    meta = {'collection': 'login'}

    def __init__(self):
        super().__init__()

    # check if password is correct
    def check_password(self, password, db):
        if bcrypt.checkpw(base64.b64encode(hashlib.sha256(self.password).digest()), db.users.find_one(
            {'username': self.username})['password']) == True or bcrypt.checkpw(base64.b64encode(hashlib.sha256(self.password).digest()), db.users.find_one(
            {'username': self.email})['password']) == True:
            flask.flash('do you want to save your login information?')