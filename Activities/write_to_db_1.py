from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Person, Activity, Location

engine = create_engine("sqlite:///activities.sqlite", echo=True)

andrew = Person(first_name="Andrew", last_name="Dales")
people = [Person(first_name="Milan", last_name="Gal"), Person(first_name="Sami", last_name="Hafezjee")]

RM1 = Location(room = "Room 1")
RM2 = Location(room = "Room 2")

fives = Activity(name = "Fives", location = RM1, attendees = people)
chess = Activity(name = "Chess", location = RM1, attendees = people)
origami = Activity(name = "Origami", location = RM2, attendees = people)

with Session(engine) as sess:
    sess.add(andrew)
    sess.add_all(people)
    sess.add(fives)
    sess.add(chess)
    sess.add(origami)
    sess.commit()