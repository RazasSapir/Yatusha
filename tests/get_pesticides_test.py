import pytest_mongodb
from Server.pesticides import *
from mongoengine import connect
from mongoengine.connection import get_db
import pytest
from Server.pesticiding_action import *

client = connect("YatushaDebug")


def test_pesticide_by_id_with_invalid_id():
    db = client.YatushaDebug
    assert get_pesticide_by_id(db=db, _id=1000) is None


def test_pesticide_by_id_with_valid_id():
    db = client.YatushaDebug
    assert get_pesticide_by_id(db=db, _id=1) is not None


def test_pesticide_actions_with_invalid_query():
    db = client.YatushaDebug
    with pytest.raises(QueryException):
        update_db(db, obj_to_change="aaa", obj_to_put="obj_to_put", obj_id="61d827415b593faea3e87e40")


if __name__ == '__main__':
    pytest.main()
