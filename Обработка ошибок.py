#1
import sqlite3
conn = sqlite3.connect('people.db')

cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS people (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        city TEXT
    )
''')

people_data = [
    ('Иван', 25, 'Москва'),
    ('Азамат', 30, 'Астана'),
    ('Сонху', 22, 'Пекин'),
]

cursor.executemany('INSERT INTO people (name, age, city) VALUES (?, ?, ?)', people_data)

conn.commit()
cursor.execute('SELECT * FROM people')

result = cursor.fetchall()

print("Список людей:")
for row in result:
    print(row)

conn.close()

#2
import sqlite3

try:
    conn = sqlite3.connect('people.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS people (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            city TEXT
        )
    ''')

    people_data = [
    ('Иван', 25, 'Москва'),
    ('Азамат', 30, 'Астана'),
    ('Сонху', 22, 'Пекин'),
    ]

    cursor.executemany('INSERT INTO people (name, age, city) VALUES (?, ?, ?)', people_data)

    conn.commit()

    cursor.execute('SELECT * FROM people')

    result = cursor.fetchall()
    print("Список людей:")
    for row in result:
        print(row)

except sqlite3.Error as e:
    print(f"Ошибка при работе с базой данных: {e}")

finally:
    if conn:
        conn.close()

#3
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:')

Base = declarative_base()

class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, Sequence('person_id_seq'), primary_key=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    city = Column(String(50))

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

try:
    people_data = [
        Person(name='Иван', age=25, city='Москва'),
        Person(name='Азамат', age=30, city='Астана'),
        Person(name='Сонху', age=22, city='Пекин'),
    ]

    session.add_all(people_data)
    session.commit()

    people_list = session.query(Person).all()
    print("Список людей:")
    for person in people_list:
        print(f"ID: {person.id}, Имя: {person.name}, Возраст: {person.age}, Город: {person.city}")

except Exception as e:
    print(f"Ошибка при работе с базой данных: {e}")

finally:
    session.close()
