import sqlite3

# Create a connection to the database
conn = sqlite3.connect("social_media.db")

# Create a cursor
cursor = conn.cursor()

# Create a SELECTION command
select_posts = """
SELECT title, description
FROM posts
"""

# Fetch all posts
posts = cursor.execute(select_posts).fetchall()

cursor.execute("SELECT comment FROM comments WHERE comment LIKE '%?';")
comments = cursor.fetchall()
for comment in comments:
    print(comment)

# Change Elizabeth’s name to Lizzy
cursor.execute("UPDATE users SET name = 'Lizzy' WHERE name = 'Elizabeth';")
conn.commit()

# Show the names of users and the number of posts they have written
cursor.execute("""
    SELECT user.name, COUNT(post.id) AS post_count
    FROM users user
    LEFT JOIN posts post ON user.id = post.user_id
    GROUP BY user.name;
""")
user_posts = cursor.fetchall()
for user, post_count in user_posts:
    print(f"User: {user}, Posts: {post_count}")

# Show the names of users and each of the comments that they have written
cursor.execute("""
    SELECT user.name, comment.comment
    FROM users user
    JOIN comments comment ON user.id = comment.user_id;
""")
user_comments = cursor.fetchall()
for user, comment in user_comments:
    print(f"User: {user}, Comment: {comment}")
conn.close()

