from pydantic import BaseModel
class CommentSchema(BaseModel):
    author_id: str
    article_id: str
    content: str
    
   