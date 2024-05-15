from pydantic import BaseModel,Field
from typing import List

class ArticleSchema(BaseModel):
    id :         str
    author_id :  str
    title :      str
    date :       str
    content :    str
    theme :      str
    note :       int
