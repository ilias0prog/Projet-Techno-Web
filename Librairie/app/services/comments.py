from app.schemas.article import ArticleSchema
from app.models.usersandarticles import Comment
from uuid import uuid4
from app.database import Session
from sqlalchemy import select
from app.services.users import get_user_id_from_cookie

def add_comment(article_id: str, comment_data: str):
    # Trouver l'id du user connecté (cookie)
    user_id = get_user_id_from_cookie()  # Assuming there is a function to get user id from cookie

    with Session() as session:
        comment = Comment(
            author_id   =user_id,
            article_id  =article_id,
            content     =comment_data
        )

    session.add(comment)
    session.commit()
    session.refresh(comment)


#def remove_comment(article_id : str, article: ArticleSchema):


#def upadte_comment(article_id : str, article: ArticleSchema):

def get_comments_by_article(article_id : str):
    with Session() as session:
        statement = select(Comment).where(Comment.article_id == article_id)
        comments = session.execute(statement).scalars().all()
        return comments


def add_comment(content: str, article_id: str, author_id : str):
    with Session() as session:
        comment = Comment(
            author_id   =author_id,
            article_id  =article_id,
            content     =content)
        session.add(comment)
        session.commit()
