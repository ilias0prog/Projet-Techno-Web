from app.Schemas.user import UserSchema
from app.Models.usersandarticles import User
from uuid import uuid4
from app.database import Session
from sqlalchemy import select
from typing import List


def get_user_by_id(id: str):
    with Session() as session:
        statement = select(User).filter_by(id=id)
        user = session.scalars(statement).one()
        if user is not None:
            return UserSchema(
                id=user.id,
                username  =user.username,
                firstname =user.firstname,
                name      =user.name,
                email     =user.email,
                password  =user.password,
                interests =user.interests,
                admin     =user.admin)
    return None


def get_user_by_username(thisUsername : str):
    with Session() as session:
        user = session.query(User).filter(User.username == thisUsername).first()
        if user is not None:
            return UserSchema (
                id        =user.id,
                username  =user.username,
                firstname =user.firstname,
                name      =user.name,
                email     =user.email,
                password  =user.password,
                interests =user.interests,
                admin     =user.admin)
            
def get_all_users():
    with Session() as session:
        statement = select(User)
        users_data = session.execute(statement).all()
        users_list = []
        for (user,) in users_data:
            user_schema = User(
                id        =user.id,
                username  =user.username,
                firstname =user.firstname,
                name      =user.name,
                email     =user.email,
                password  =user.password,
                interests =user.interests,
                admin     =user.admin)
            users_list.append(user_schema)
            
        return users_list
    
def register(username: str,
             firstname: str,
             name: str,
             email: str,
             password: str,
             confirm_your_password: str,
             interests: List[str]):
    maxLengthPassword = 20
    minLengthPassword = 8
    
    if password != confirm_your_password:
        raise ValueError("The passwords do not match.")
    
    elif len(password) < minLengthPassword or len(password) > maxLengthPassword:
        raise ValueError("The length of the password must be between {} and {}".format(minLengthPassword,maxLengthPassword))
    
    for user in get_all_users():
        if user["username"] == username or user["email"] == email:
            raise ValueError ("This username or email is already taken.")
    else :
        with Session() as session:
            user = User(
                id=str(uuid4()),
                username=username,
                firstname=firstname,
                name=name,
                email=email,
                password=password,
                interests=[i.lower() for i in interests],
                admin=False)
            session.add(user)
            session.commit()
            
def grant_admin(id: str):
    with Session() as session:
        statement = select(User).filter_by(id=id)
        user = session.scalars(statement).one()
        if user is not None:
            user.admin = True
            session.commit()