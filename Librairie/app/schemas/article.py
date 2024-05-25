from pydantic import BaseModel,Field
from typing import List
from datetime import date as Date


class ArticleSchema(BaseModel):
    id :                str
    author_username :   str
    title :             str
    date :              Date
    content :           str
    theme :             str
 