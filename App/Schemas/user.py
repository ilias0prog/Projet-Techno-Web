from pydantic import BaseModel,Field
from typing import List

class UserSchema(BaseModel):
    id :        str
    username :  str
    firstname : str
    name :      str
    email :     str
    password :  str
    interests : List[str]
    admin :     bool = False