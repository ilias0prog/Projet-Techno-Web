from app.schemas.article import ArticleSchema
from app.schemas.user import UserSchema
from app.models.usersandarticles import Article
from uuid import uuid4
from app.database import Session
from sqlalchemy import select
import random


def get_all_articles():
    with Session() as session:
        statement = select(Article)
        articles_data = session.scalars(statement).all()
        articles_list = [
            Article(
                id              =article.id,
                author_username =article.author_username,
                title           =article.title,
                date            = article.date,
                content         =article.content,
                theme           =article.theme,
                likes           =article.likes,
                dislikes        =article.dislikes)
            for article in articles_data]
        
        random.shuffle(articles_list)
        return articles_list
        
        
def get_all_articles_by_author(user):
    with Session() as session:
        statement = select(Article).where(Article.author_username == user.username)
        articles_data = session.scalars(statement).all()
        articles_list = [
            Article(
                id              =article.id,
                author_username =article.author_username,
                title           =article.title,
                date            = article.date,
                content         =article.content,
                theme           =article.theme,
                likes           =article.likes,
                dislikes        =article.dislikes)
            for article in articles_data]
        
        random.shuffle(articles_list)
        return articles_list


def get_all_articles_by_themes(themes: list):
    with Session() as session:
        statement = select(Article).where(Article.theme.in_(themes))
        articles_data = session.execute(statement).scalars().all()
        articles_list = [
            Article(
                id              =article.id,
                author_username =article.author_username,
                title           =article.title,
                date            = article.date,
                content         =article.content,
                theme           =article.theme,
                likes           =article.likes,
                dislikes        =article.dislikes)
            for article in articles_data]
        
        random.shuffle(articles_list)
        return articles_list
    
def get_all_articles_by_date(data):
    with Session() as session:
        statement = select(Article).where(Article.date == data)
        articles_data = session.execute(statement).scalars().all()
        articles_list = [
            Article(
                id              =article.id,
                author_username =article.author_username,
                title           =article.title,
                date            = article.date,
                content         =article.content,
                theme           =article.theme,
                likes           =article.likes,
                dislikes        =article.dislikes)
            for article in articles_data]
        
        random.shuffle(articles_list)
        return articles_list
    

# def change_date_format(date : str):
#     date_list = date.split('-')
#     return f'{date_list[2]}.{date_list[1]}.{date_list[0]}'

        

def get_article_by_id(article_id: str) -> ArticleSchema | None:
    """
    Récupère un article à partir de son ID.

    Args:
        article_id (str): L'identifiant de l'article à récupérer.

    Returns:
        ArticleSchema | None: L'objet article s'il est trouvé, None sinon.
    """
    with Session() as session:
        statement = select(Article).filter_by(id=article_id)
        article = session.scalar(statement) 
        if article is not None:
            return ArticleSchema(
                id=article.id,
                author_username   = article.author_username,
                title=article.title,
                date=article.date,
                content=article.content,
                theme=article.theme,
                
            )
    return None


def add_article (article: ArticleSchema) -> ArticleSchema:
    with Session() as session:
        new_article = Article(
            id = str(uuid4()),
            author_username   = article.author_username,
            title = article.title,
            date = article.date,
            content = article.content,
            theme = article.theme
        )
        session.add(new_article)
        session.commit()

def delete_article(article_id: str):
    with Session() as session:
        statement = select(Article).where(Article.id == article_id)
        article = session.scalars(statement).first()
        session.delete(article)
        session.commit()

def update_article(article_id: str, title: str, content: str):
    with Session() as session:
        statement = select(Article).where(Article.id == article_id)
        article = session.scalars(statement).first()
        article.title = title
        article.content =content
        session.commit()

def like_article(article_id : str, article: ArticleSchema):
    with Session() as session:
        statement = select(Article).where(Article.id == article_id)
        article = session.scalars(statement).first()
        article.likes += 1
        session.commit()

def unlike_article(article_id : str, article: ArticleSchema):
    with Session() as session:
        statement = select(Article).where(Article.id == article_id)
        article = session.scalars(statement).first()
        article.likes -= 1
        session.commit

def dislike_article(article_id : str, article: ArticleSchema):
    with Session() as session:
        statement = select(Article).where(Article.id == article_id)
        article = session.scalars(statement).first()
        article.dislikes += 1
        session.commit()

def undislike_article(article_id : str, article: ArticleSchema):
    with Session() as session:
        statement = select(Article).where(Article.id == article_id)
        article = session.scalars(statement).first()
        article.dislikes -= 1
        session.commit()
