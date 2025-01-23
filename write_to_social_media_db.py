conn = sqlite3.connect('users.sqlite')
cursor = conn.cursor()

parameterised_insert_query_users = """
INSERT INTO
    users(name, age, gender, nationality)
Values 
    (?, ?, ?, ?);
"""

User_Values = [('James', 25, 'male', 'USA'),
        ('Leila', 32, 'female', 'France'),
        ('Brigitte', 35, 'female', 'England'),
        ('Mike', 40, 'male', 'Denmark'),
        ('Elizabeth', 21, 'female', 'Canada'),
        ]

for i in User_Values:
    cursor.execute(parameterised_insert_query_users, i)

conn.commit()

insert_query = """
INSERT INTO
  posts (title, description, user_id)
VALUES
  ("Happy", "I am feeling very happy today", 1);
"""

parameterised_insert_query_posts = """
INSERT INTO
    posts(title, description, user_id)
Values 
    (?, ?, ?);
"""

post_values = [('Happy', 'I am feeling very happy today', 1),
               ('Hot Weather', 'The weather is very hot today', 2),
               ('Help', 'I need some help with my work', 2),
               ('Great News', 'I am getting married', 1),
               ('Interesting Game', 'It was a fantastic game of tennis', 5),
               ('Party', 'Anyone up for a late-night party today?', 3),
                ]

for i in post_values:
    cursor.execute(parameterised_insert_query_posts, i)

conn.commit()

comment_insert = """
    INSERT INTO comments(comment, user_id, post_id)
    VALUES
    ('Count me in', 1, 6),
    ('What sort of help?', 5, 3),
    ('Congrats buddy', 2, 4),
    ('I was rooting for Nadal though', 4, 5),
    ('Help with your thesis?', 2, 3),
    ('Many congratulations', 5, 4);
    """

conn.commit()

likes_insert = """
    INSERT INTO likes(user_id, post_id)
    VALUES
    (1, 6),
    (2, 3),
    (1, 5),
    (5, 4),
    (2, 4),
    (4, 2),
    (3, 6);
    """

conn.commit()

conn.close()
