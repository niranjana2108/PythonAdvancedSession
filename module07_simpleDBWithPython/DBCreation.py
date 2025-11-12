import sqlite3

# Step 1: Connect to database (creates file if not exists)
conn = sqlite3.connect("students1.db")

# Step 2: Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Step 3: Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    department TEXT,
    marks REAL
)
''')
print("Table created successfully.")

# Step 4: Insert data
cursor.execute("INSERT INTO students (name, age, department, marks) VALUES (?, ?, ?, ?)",
               ("Rahul", 21, "Computer Science", 88.5))
cursor.execute("INSERT INTO students (name, age, department, marks) VALUES (?, ?, ?, ?)",
               ("Priya", 22, "Commerce", 91.0))
cursor.execute("INSERT INTO students (name, age, department, marks) VALUES (?, ?, ?, ?)",
               ("Karthik", 20, "Engineering", 76.4))
conn.commit()
print("Data inserted successfully.")

# Step 5: Read data
print("\nAll Students:")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# Step 6: Update data
cursor.execute("UPDATE students SET marks = ? WHERE name = ?", (95.0, "Priya"))
conn.commit()
print("\nUpdated Priya's marks.")

# Step 7: Delete data
cursor.execute("DELETE FROM students WHERE name = ?", ("Karthik",))
conn.commit()
print("Deleted Karthik's record.")

# Step 8: Display remaining records
print("\nRemaining Students:")
cursor.execute("SELECT * FROM students ORDER BY marks DESC")
for row in cursor.fetchall():
    print(row)

# Step 9: Close connection
conn.close()
print("\nConnection closed.")
