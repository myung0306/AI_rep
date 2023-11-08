import sqlite3
from value_object import Student

db_path

def select_student(limit, offset):
    conn = None
    try:
        conn = sqlite3.connect(db_path)

        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(student_id) FROM STUDENT;""")
        count = cursor.fetchall()[0][0]

        sql = """SELECT * FROM STUDENT
                          ORDER BY student_id
                          LIMIT ?
                          OFFSET ?;"""
        cursor = conn.cursor()
        cursor.execute(sql, (limit, offset))
        students = []
        for row in cursor.fetchall():
            students.append(Student(row[0], row[1], row[2], row[3]))

        return (limit, offset, count, students)
    except Exception as e:
        raise e
    finally:
        if conn:
            conn.close()