import pytest
import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from model_sm import User, Post, Comment, Base

test_db_location = 'sqlite:///social_media.db'

def test_test():
    assert 1 == 1

class TestDatabase:
    @pytest.fixture(scope='class')
    def db_session(self):
        engine = sa.create_engine(test_db_location)
        Base.metadata.create_all(engine)
        session = Session(engine)
        yield session # Like a return but when you call again, it comes back to the yield point
        session.close()

    def test_valid_user(self, db_session):
        user = User(name = "John", age = 20, gender = "male")
        db_session.add(user)
        db_session.commit()
        qry = sa.select(User).where(User.name == "John")
        John = db_session.scalar(qry)
        assert John is not None
        assert John.name == "John"
        assert John.age == 20
        assert John.gender == "male"
        assert John.nationality is None