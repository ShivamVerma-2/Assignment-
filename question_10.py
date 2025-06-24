import sqlite3

conn = sqlite3.connect("shivam.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY,
    course_name TEXT,
    credits INTEGER
)
""")

print("Database and tables created.")



#  10.1
cursor.execute("INSERT INTO students (name, age) VALUES ('Shivam', 20)")
cursor.execute("INSERT INTO students (name, age) VALUES ('Verma', 22)")
cursor.execute("INSERT INTO courses (course_name, credits) VALUES ('Math', 4)")
cursor.execute("INSERT INTO courses (course_name, credits) VALUES ('DSA', 3)")

conn.commit()
print("Records inserted.")

#  10.2

cursor.execute("SELECT * FROM students")
print("Students:")
for row in cursor.fetchall():
    print(row)

#10.3
cursor.execute("SELECT * FROM students WHERE age > 21")
print("\nStudents older than 21:")
for row in cursor.fetchall():
    print(row)

#  10.4
cursor.execute("UPDATE students SET age = 21 WHERE name = 'Alice'")
conn.commit()
print("Updated Alice's age to 21.")



cursor.execute("DELETE FROM students WHERE name = 'Bob'")
conn.commit()
print("Deleted student named Bob.")
