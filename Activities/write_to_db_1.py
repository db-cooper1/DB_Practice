from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Person

andrew = Person(first_name="Andrew", last_name="Dales")
people = [Person(first_name="Milan", last_name="Gal"), Person(first_name="Sami", last_name="Hafezjee")]

fives = Activity(name = "fives", location = "Room 5", location_id = 1, attendees = people)
chess = Activity(name = "chess", location = "Room 5", location_id = 1, attendees = andrew)
origami = Activity(name = "chess", location = "Library", location_id = 2, attendees = [people[0], andrew])


engine = create_engine("sqlite:///activities.sqlite", echo=True)

with Session(engine) as sess:
    sess.add(andrew)
    sess.add_all(people)
    sess.add(fives)
    sess.add(chess)
    sess.add(origami)
    sess.commit()