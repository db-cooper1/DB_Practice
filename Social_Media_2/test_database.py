import pytest
import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from Social_Media_2.write_sm_db import write_initial_data
from Social_Media_2.controller import Controller
from model_sm import User, Post, Comment, Base

test_db_location = 'sqlite:///test_database.db'

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


# test for uniqueness in the users identity / name etc

class TestController:
    @pytest.fixture(scope='class', autouse=True)
    def test_db(self):
        engine = sa.create_engine(test_db_location)
        Base.metadata.create_all(engine)
        write_initial_data(engine)
        yield
        Base.metadata.drop_all(engine)

    @pytest.fixture(scope='class')
    def controller(self):
        control = Controller(db_location = 'test_database_location')
        return control
    def test_set_current_user_from_name(self, control):
        control.set_current_user_from_name("Alice")
        assert "ALice" == control.current_user.name
        assert 30 == control.current_user.age
        assert "Female" == control.current_user.gender
        assert "Canadian" == control.current_user.nationality

    def test_get_user_names(self):
        assert True

    def test_create_user(self):
        assert True

    def test_get_posts(self):
        assert True
