import sqlite3

with sqlite3.connect("students.sqlite") as conn:
    cursor = conn.cursor()

    #7

    j_firstname = """
    SELECT firstname
    FROM students
    WHERE firstname LIKE 'J%'
    """
    names = cursor.execute(j_firstname).fetchmany(5)
    print(names)

    #8

    gender_group = """
    SELECT gender
    FROM students
    """
    students_gender=cursor.execute(gender_group).fetchall()
    print(f"Male: {students_gender.count(('M' ,))}, Female: {students_gender.count(('F' ,))}")

    #9

    group_by = """
    SELECT substring(firstname, 1,1), SUM(age)
    FROM students
    GROUP BY substring(firstname, 1, 1)
    """
    sum_ages = cursor.execute(group_by).fetchall()
    print(sum_ages)
