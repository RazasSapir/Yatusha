# import bcrypt and mongoengine
import bcrypt
import mongoengine
import base64
import hashlib
import pymongo.database


Database = pymongo.database.Database


class UsersDb(mongoengine.Document):
    email = mongoengine.EmailField(required=True)
    password = mongoengine.StringField(required=True)
    username = mongoengine.StringField(required=True)
    meta = {'collection': 'users'}

    def __init__(self, email: str, password: str, username: str) -> None:
        """
        Initialize the user
        :param email: the email of the user
        :param password: the password of the user
        :param username: the username of the user
        """
        super().__init__()
        self.email = email
        self.password = password
        self.hash_password()
        self.username = username

    def __call__(self, db: Database) -> bool:
        """
        Return the user's information
        :return: the user's information
        """
        return self.check_email() is None

    def check_email(self, db: Database) -> dict:
        """
        Check if the email is in the database
        :return: if the email is in the database
        """
        users = db.users
        return users.findOne({'email': self.email})

    def hash_password(self) -> None:
        """
        Hash the password
        :return: hashed password
        """
        self.password = bcrypt.hashpw(
            base64.b64encode(hashlib.sha256(self.password).digest()),
            bcrypt.gensalt()).decode('utf-8')

    def edit_user(self, email: str, password: str, username: str) -> None:
        """
        Edit the user's information
        :param email: the new email of the user
        :param password: the new password of the user
        :param username: the new username of the user
        :return: None
        """
        if email != '' and email is not None:
            self.email = email

        if password != '' and password is not None:
            self.password = password
            self.hash_password()

        if username != '' and username is not None:
            self.username = username

        self.save()

    def delete_user(self) -> None:
        """
        Delete the user
        :return: None
        """
        self.delete()

    # create a methos to verify the user by using the mail verify link with his user id
    def verify_user(self, db: Database) -> bool:
        """
        Verify the user
        :return: if the user is verified
        """
        users = db.users
        return users.update_one({'email': self.email}, {'$set': {'verified': True}})

    def get_user_verification_status(self, db: Database, email: str) -> bool:
        """
        Get the user's verification status
        :return: if the user is verified
        """
        users = db.users
        return users.find_one({'email': email})['verified']

