from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Person

andrew = Person(first_name="Andrew", last_name="Dales")
people = [Person(first_name="Milan", last_name="Gal"), Person(first_name="Sami", last_name="Hafezjee")]

engine = create_engine("sqlite:///activities.sqlite", echo=True)

with Session(engine) as sess:
    sess.add(andrew)
    sess.add_all(people)
    sess.commit()