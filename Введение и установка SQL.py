from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

class Person(Base):
    __tablename__ = "people"
    id = Column(Integer, Sequence("person_id_seq"), primary_key=True)
    name = Column(String(50))
    occupation = Column(String(50))

engine = create_engine("sqlite:///:memory:", echo=True)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

user145 = User(name="Джон Сноу", age=19)
user135 = User(name="Дэйенерис Таргариен", age=18)
session.add_all([user145, user135])

person1 = Person(name="Ария Старк", occupation="Безликий")
person2 = Person(name="Брандон Старк", occupation="Трехглазый ворон")
session.add_all([person1, person2])

session.commit()

users = session.query(User).all()
for user in users:
    print(f"User {user.id}: {user.name}, {user.age} лет.")

people = session.query(Person).all()
for person in people:
    print(f"Персонаж {person.id}: {person.name}, {person.occupation}")
