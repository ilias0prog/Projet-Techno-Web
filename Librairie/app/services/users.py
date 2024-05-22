from sqlalchemy import select
from uuid import uuid4
from app.database import Session
from app.models.usersandarticles import User
from app.schemas.user import UserSchema
from fastapi import Request, HTTPException

def get_user_id_from_cookie(request: Request) -> str:
    user_id = request.cookies.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="User ID cookie not found")
    return user_id


def get_user_by_username(username: str):
    with Session() as session:
        statement = select(User).filter_by(username=username)
        user = session.scalar(statement) 
        if user is not None:
            return UserSchema(
                id = user.id,
                username=user.username,
                firstname = user.firstname,
                name = user.name,
                email = user.email,
                password = user.password,
            )
    return None



    
def get_user_by_id(id: str):
    with Session() as session:
        statement = select(User).filter_by(id=id)
        user = session.scalars(statement).one()
        #user = session.query(User).filter_by(id=id).first()
        if user is not None:
            return UserSchema(
                id=user.id,
                username=user.username,
                firstname=user.firstname,
                name=user.name,
                email=user.email,
                password=user.password,
                interests= user.interests,
                admin=user.admin,
            )
    return None


def get_user_by_username(thisUsername: str):
    with Session() as session:
        try:
            user = session.query(User).filter(User.username == thisUsername).first()
            if user is not None:
                # Log the user to verify it's correct
                print(f"Fetched user: {user}")
                return UserSchema(
                    id=user.id,
                    username=user.username,
                    firstname=user.firstname,
                    name=user.name,
                    email=user.email,
                    password=user.password,
                    interests=user.interests,
                    admin=user.admin,
                    articles=user.articles,
                )
            else:
                print("User not found")
                return None
        except Exception as e:
            print(f"Error fetching user by username: {e}")
            return None


    
        


def register(username: str, firstname: str, name: str,email: str, password: str, confirm_your_password: str):
    # Adds a new username to the database
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
                password=password
            )
            session.add(user)
            session.commit()
    
def get_all_users():
    # Returns all the users as a list
    with Session() as session:
        statement = select(User)
        users_data = session.execute(statement).all()
        users_list = []
        for (user,) in users_data:
            
            user_schema = User(
                id=user.id,
                username=user.username,
                firstname=user.firstname,
                name=user.name,
                email=user.email,
                password=user.password,
                interests = user.interests,
                admin =user.admin,
                articles = user.articles,
            )
            users_list.append(user_schema)
        
        return users_list
        

def grant_admin(id : str):
    # promote admin the user with the given username
    with Session() as session:
        statement = select(User).filter_by(id=id)
        user = session.scalars(statement).one()
        
        if user is not None:
            user.admin = True
            session.commit()
            return True 
        else:
            return False


