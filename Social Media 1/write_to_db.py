import sqlite3
from faker import Faker
import random
fake = Faker("en_GB")

conn = sqlite3.connect('students.sqlite')

with sqlite3.connect('students.sqlite') as conn:
    cursor = conn.cursor()
    insert_query = """
    INSERT INTO students (firstname,lastname ,age,gender)
    VALUES
    ('Milan','Gal',17,'male'),
    ('Eleanore','Shiner',16,'female'),
    ('RayBan','Chowdhury','16','male'),
    ('Denys','Zazuliak',17,'male'),
    ('Adam','Reeves',16,'e-girl'),
    ('Sami','Hafezje',16,'male');
    """

    conn.commit()

parameterised_insert_query = """

INSERT INTO
    students(firstname, lastname, age, gender)
Values 
    (?, ?, ?, ?);
"""

conn = sqlite3.connect('students.sqlite')
cursor = conn.cursor()

fake.random.seed(4321)
random.seed(4321)
for _ in range(100):
        f=fake.profile()
        cursor.execute(parameterised_insert_query, [*f['name'].split(' ')[-2:], random.randint(11,18), f['sex']])

conn.commit()
conn.close()