import sqlite3
from tabulate import tabulate

def execute_read_query(conn, query):
    cursor = conn.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")


select_users = "SELECT * from users"
with sqlite3.connect("sm_app.sqlite") as conn:
    users = execute_read_query(conn, select_users)

for user in users:
    print(user)

select_posts = "SELECT * FROM posts"
with sqlite3.connect("sm_app.sqlite") as conn:
    posts = execute_read_query(conn, select_posts)

for post in posts:
    print(post)

select_users_posts = """
SELECT
users.id,
users.name,
posts.description
FROM
posts
INNER JOIN users ON users.id = posts.user_id
"""


users_posts = execute_read_query(conn, select_users_posts)
for users_post in users_posts:
    print(users_post)

select_posts_comments_users = """
SELECT
posts.description as post, comments.comment as comment, users.name as name
FROM
posts
INNER JOIN comments ON posts.id = comments.post_id
INNER JOIN users ON users.id = comments.user_id
"""
with sqlite3.connect("sm_app.sqlite") as conn:
    posts_comments_users = execute_read_query(conn, select_posts_comments_users)


for posts_comments_user in posts_comments_users:
    print(posts_comments_user)

cursor = conn.cursor()
cursor.execute(select_posts_comments_users)
cursor.fetchall()
column_names = [description[0] for description in cursor.description]
print(column_names)

select_post_likes = """

SELECT
description as Post, COUNT(likes.id) as Likes
FROM
likes, posts
WHERE
posts.id = likes.post_id
GROUP BY
likes.post_id
"""

post_likes = execute_read_query(conn, select_post_likes)

for post_like in post_likes:
    print(post_like)