import sqlite3

conn = sqlite3.connect("mydatabase_1.db")
cursor = conn.cursor()

create_table_query = '''
CREATE TABLE IF NOT EXISTS Products (
    ID INTEGER PRIMARY KEY,
    Name TEXT,
    Price REAL
);
'''
cursor.execute(create_table_query)

insert_data_query = '''
INSERT INTO Products (ID, Name, Price) VALUES
    (5, "Tablet", 299.99),
    (7, "Camera", 799.99);
'''
cursor.execute(insert_data_query)
conn.commit()
cursor.close()
conn.close()
