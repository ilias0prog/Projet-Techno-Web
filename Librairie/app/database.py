#from uuid import uuid4
from sqlalchemy import create_engine 
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from uuid import uuid4
from datetime import datetime

engine = create_engine(
    #"sqlite:///data/database.sqlite", 
    "sqlite:///Librairie\data\database.sqlite", 
    echo=True
)

Session = sessionmaker(engine)

class Base(DeclarativeBase):
    pass

from app.models.usersandarticles import  User
from app.models.usersandarticles import  Article




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
        
    },
    {
        "id": str(uuid4()),
        "username": "jane_smith",
        "firstname": "Jane",
        "name": "Smith",
        "email": "jane.smith@example.com",
        "password": "password456",
        "admin": False,
        
    },
    {
        "id": str(uuid4()),
        "username": "bob_johnson",
        "firstname": "Bob",
        "name": "Johnson",
        "email": "bob.johnson@example.com",
        "password": "password789",
        "admin": False,
        
    },
    {
        "id": str(uuid4()),
        "username": "emily_clark",
        "firstname": "Emily",
        "name": "Clark",
        "email": "emily.clark@example.com",
        "password": "passwordabc",
        "admin": True,
       
    },
    {
        "id": str(uuid4()),
        "username": "michael_taylor",
        "firstname": "Michael",
        "name": "Taylor",
        "email": "michael.taylor@example.com",
        "password": "passworddef",
        "admin": False,
        
    },
    {
        "id": str(uuid4()),
        "username": "susan_miller",
        "firstname": "Susan",
        "name": "Miller",
        "email": "susan.miller@example.com",
        "password": "passwordghi",
        "admin": False,
        
    },
    {
        "id": str(uuid4()),
        "username": "david_anderson",
        "firstname": "David",
        "name": "Anderson",
        "email": "david.anderson@example.com",
        "password": "passwordjkl",
        "admin": True,
       
    },
    {
        "id": str(uuid4()),
        "username": "amy_wilson",
        "firstname": "Amy",
        "name": "Wilson",
        "email": "amy.wilson@example.com",
        "password": "passwordmno",
        "admin": False,
        
    },
    {
        "id": str(uuid4()),
        "username": "peter_brown",
        "firstname": "Peter",
        "name": "Brown",
        "email": "peter.brown@example.com",
        "password": "passwordpqr",
        "admin": False,
        
    },
    {
        "id": str(uuid4()),
        "username": "laura_evans",
        "firstname": "Laura",
        "name": "Evans",
        "email": "laura.evans@example.com",
        "password": "passwordstu",
        "admin": True,
        
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
                interests  = "",
                admin=user_data["admin"],
                )
            session.add(user)
            session.commit()

def fill_articles_db():
    # Assurez-vous que les utilisateurs existent dans la base de donnees
    with Session() as session:
        users = session.query(User).all()
        if not users:
            print("No users found in the database. Please add users before adding articles.")
            return
        articles_data = [
                {
                    "author_id": users[0].id, 
                    "title": "The Future of Technology",
                    "date": datetime.now(),
                    "content": "A deep dive into the future trends of technology.",
                    "theme": "technology",
                    "likes": 4,
                    "dislikes": 1
                },
                {
                    "author_id": users[1].id,
                    "title": "Health Benefits of Yoga",
                    "date": datetime.now(),
                    "content": "Exploring the numerous health benefits of practicing yoga.",
                    "theme": "health",
                    "likes": 5,
                    "dislikes": 0
                },
                {
                    "author_id": users[2].id,
                    "title": "Political Landscape in 2024",
                    "date": datetime.now(),
                    "content": "An analysis of the current political trends and future projections.",
                    "theme": "politics",
                    "likes": 3,
                    "dislikes": 0
                },
                {
                    "author_id": users[3].id,
                    "title": "Environmental Challenges",
                    "date": datetime.now(),
                    "content": "Addressing the major environmental challenges we face today.",
                    "theme": "environment",
                    "likes": 4,
                    "dislikes": 0
                },
                {
                    "author_id": users[4].id,
                    "title": "Economic Growth Post-Pandemic",
                    "date": datetime.now(),
                    "content": "How the world economies are recovering after the pandemic.",
                    "theme": "economics",
                    "likes": 4,
                    "dislikes": 0
                },
                {
                    "author_id": users[5].id,
                    "title": "Social Media and Society",
                    "date": datetime.now(),
                    "content": "The impact of social media on modern society.",
                    "theme": "social",
                    "likes": 3,
                    "dislikes": 0
                },
                {
                    "author_id": users[6].id,
                    "title": "International Relations in a Globalized World",
                    "date": datetime.now(),
                    "content": "The dynamics of international relations in today's globalized world.",
                    "theme": "international",
                    "likes": 5,
                    "dislikes": 0
                },
                {
                    "author_id": users[7].id,
                    "title": "The Cultural Significance of Art",
                    "date": datetime.now(),
                    "content": "Understanding the cultural importance and influence of art.",
                    "theme": "culture",
                    "likes": 4,
                    "dislikes": 0
                },
                {
                    "author_id": users[8].id,
                    "title": "The Evolution of Sports",
                    "date": datetime.now(),
                    "content": "A look into how sports have evolved over the years.",
                    "theme": "sport",
                    "likes": 4,
                    "dislikes": 0
                }
            ]
        with Session() as session:
            for article_data in articles_data:
                article = Article(
                    author_id=article_data["author_id"],
                    title=article_data["title"],
                    date=article_data["date"],
                    content=article_data["content"],
                    theme=article_data["theme"],
                    likes=article_data["likes"],
                    dislikes=article_data["dislikes"],)
                session.add(article)
                session.commit()