import sqlite3
import csv

conn = sqlite3.connect("mydatabase_2.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Employees (
    EmployeeID INTEGER PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT,
    DepartmentID INTEGER
);
''')

with open("26.csv", "r") as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        cursor.execute(
            "INSERT INTO Employees (EmployeeID, FirstName, LastName, DepartmentID) VALUES (?, ?, ?, ?);",
            (row["EmployeeID"], row["FirstName"], row["LastName"], row["DepartmentID"])
        )

conn.commit()
conn.close()
