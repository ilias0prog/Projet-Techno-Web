from app.schemas.article import ArticleSchema
from app.models.usersandarticles import Article
from uuid import uuid4
from app.database import Session
from sqlalchemy import select


def get_all_articles():
    with Session() as session:
        statement = select(Article)
        articles_data = session.scalars(statement).all()
        return [
            Article(
                id          = article.id,
                author_id   = article.author_id,
                title       = article.title,
                date        = article.date,
                content     = article.content,
                theme       = article.theme,
                note        = article.note)
            for article in articles_data]
        
        
def get_all_articles_by_theme(theme :str):
    if theme in ("sport", "culture", "politics", "economics", "health", "environment", "social", "technology", "international"):
        with Session() as session:
            statement = select(Article).where(Article.theme == theme)
            articles_data = session.scalars(statement).all()
            return [
                Article(
                    id          = article.id,
                    author_id   = article.author_id,
                    title       = article.title,
                    date        = article.date,
                    content     = article.content,
                    theme       = article.theme,
                    note        = article.note)
                for article in articles_data]
        

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
                author_id=article.author_id,
                title=article.title,
                date=article.date,
                content=article.content,
                theme=article.theme,
                note=article.note
            )
    return None


def add_article (article: ArticleSchema) -> ArticleSchema:
    with Session() as session:
        new_article = Article(
            id = str(uuid4()),
            author_id = article.author_id,
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

def update_article(article_id: str, article: ArticleSchema):
    with Session() as session:
        statement = select(Article).where(Article.id == article_id)
        article = session.scalars(statement).first()
        article.title = article.title
        article.date = article.date
        article.content = article.content
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
