from pydantic import BaseModel,Field
from typing import List, Optional

class UserSchema(BaseModel):
    id :        str
    username :  str
    firstname : str
    name :      str
    email :     str
    password :  str
    interests : Optional[str] = None    
    admin :     bool = False