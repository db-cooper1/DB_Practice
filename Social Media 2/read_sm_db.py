import sqlalchemy as sa
import sqlalchemy.orm as so
from model_sm import User, Post, Comment, Base

# Create an engine
engine = sa.create_engine('sqlite:///social_media.db')
session = so.Session(bind=engine)

# Query and print all users
users = session.scalars(sa.select(User)).all()
for user in users:
    print(user)

# Query and print all posts
posts = session.scalars(sa.select(Post)).all()
for post in posts:
    print(post)

# Query and print all comments
comments = session.scalars(sa.select(Comment)).all()
for comment in comments:
    print(comment)

# when you have the structure for a controller (gui or cli) do integration testing instead of unit testing