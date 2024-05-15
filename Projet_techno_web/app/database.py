#from uuid import uuid4
from sqlalchemy import create_engine 
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from uuid import uuid4


engine = create_engine(
    "sqlite:///Projet_techno-web\Data\database.sqlite", 
    echo=True
)

Session = sessionmaker(engine)

class Base(DeclarativeBase):
    pass
from app.Models.usersandarticles import User




def create_database():
    Base.metadata.create_all(engine)

def clear_database():
    Base.metadata.clear()
    
def delete_database():
    Base.metadata.drop_all(engine)

def fill_users_db():    
    users_data = [
    {
        "id": str(uuid4()),
        "username": "john_doe",
        "firstname": "John",
        "name": "Doe",
        "email": "john.doe@example.com",
        "password": "password123",
        "admin": True,
        "blocked": False
    },
    {
        "id": str(uuid4()),
        "username": "jane_smith",
        "firstname": "Jane",
        "name": "Smith",
        "email": "jane.smith@example.com",
        "password": "password456",
        "admin": False,
        "blocked": False
    },
    {
        "id": str(uuid4()),
        "username": "bob_johnson",
        "firstname": "Bob",
        "name": "Johnson",
        "email": "bob.johnson@example.com",
        "password": "password789",
        "admin": False,
        "blocked": True
    },
    {
        "id": str(uuid4()),
        "username": "emily_clark",
        "firstname": "Emily",
        "name": "Clark",
        "email": "emily.clark@example.com",
        "password": "passwordabc",
        "admin": True,
        "blocked": True
    },
    {
        "id": str(uuid4()),
        "username": "michael_taylor",
        "firstname": "Michael",
        "name": "Taylor",
        "email": "michael.taylor@example.com",
        "password": "passworddef",
        "admin": False,
        "blocked": False
    },
    {
        "id": str(uuid4()),
        "username": "susan_miller",
        "firstname": "Susan",
        "name": "Miller",
        "email": "susan.miller@example.com",
        "password": "passwordghi",
        "admin": False,
        "blocked": False
    },
    {
        "id": str(uuid4()),
        "username": "david_anderson",
        "firstname": "David",
        "name": "Anderson",
        "email": "david.anderson@example.com",
        "password": "passwordjkl",
        "admin": True,
        "blocked": False
    },
    {
        "id": str(uuid4()),
        "username": "amy_wilson",
        "firstname": "Amy",
        "name": "Wilson",
        "email": "amy.wilson@example.com",
        "password": "passwordmno",
        "admin": False,
        "blocked": False
    },
    {
        "id": str(uuid4()),
        "username": "peter_brown",
        "firstname": "Peter",
        "name": "Brown",
        "email": "peter.brown@example.com",
        "password": "passwordpqr",
        "admin": False,
        "blocked": True
    },
    {
        "id": str(uuid4()),
        "username": "laura_evans",
        "firstname": "Laura",
        "name": "Evans",
        "email": "laura.evans@example.com",
        "password": "passwordstu",
        "admin": True,
        "blocked": False
    }
]
    
    with Session() as session:
        for user_data in users_data:
            user = User(
    id=user_data["id"],
    username=user_data["username"],
    firstname=user_data["firstname"],
    name=user_data["name"],
    email=user_data["email"],
    password=user_data["password"],
    admin=user_data["admin"],
    blocked=user_data["blocked"],
    theme =[],)
            session.add(user)
        session.commit()
