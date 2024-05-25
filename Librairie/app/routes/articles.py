from typing import Annotated
from fastapi import APIRouter, HTTPException, status, Depends, Form
from fastapi.responses import RedirectResponse, JSONResponse, PlainTextResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates
from app.schemas.article import *
from Templates import *
from app.login_manager import *
from app.services import articles as service
from app.services.users import get_user_by_id
from app.services.comments import *
from app.schemas.user import UserSchema
from app.schemas.article import ArticleSchema
from app.schemas.comment import CommentSchema
from app.services.comments import *
from uuid import uuid4
from datetime import datetime
from app.models.usersandarticles import Article, Comment, User


templates = Jinja2Templates(directory="Librairie\Templates")
router = APIRouter(prefix="/articles", tags=["articles"])


# @router.get("/homepage")
# def get_feed(request : Request, user: UserSchema = Depends(login_manager)):
#     # Fetch connected user info with cookie 
#     themes = user.interests.split(' ')
#     articles = service.get_all_articles_by_themes(themes)

#     # comments = []
#     # for article in articles:
#     #     for comment in get_comments_by_article(article.id):
#     #         comments.append[comment]
#     comments = {}
#     for article in articles:
#         comments[article.id] = get_comments_by_article(article.id)

#     return templates.TemplateResponse("/homepage.html", context = {"request" : request, "articles" : articles, "user" : user, "comments" : comments})

@router.get("/homepage/{filter}/{data}")
def get_feed(request : Request, filter : str, data :str,  user: UserSchema = Depends(login_manager)):
    # Fetch connected user info with cookie 
    if filter == 'search_theme':
        articles = service.get_all_articles_by_themes([data])
    elif filter == 'search_date':
        articles = service.get_all_articles_by_date(data)
    else:
        themes = user.interests.split(' ')
        articles = service.get_all_articles_by_themes(themes)

    articles = [article for article in articles if article.author_username != user.username] 

    comments = {}
    for article in articles:
        comments[article.id] = get_comments_by_article(article.id)

    return templates.TemplateResponse("/homepage.html", context = {"request" : request, "articles" : articles, "user" : user, "comments" : comments})

@router.post("/load_comments/{article_id}")
async def load_comments(article_id: str):
    comments = get_comments_by_article(article_id)
    return {"comments": comments}

# @router.post("/post_comment")
# async def post_comment(request : Request, content : str, article_id : str, user : UserSchema = Depends(login_manager)):
#     comment = CommentSchema(author_id=user.id, article_id=article_id, content = content)
#     add_comment(content, article_id, user.id)
#     return comment

@router.post("/post_comment")
async def post_comment(request: Request, content: str, article_id: str, user: UserSchema = Depends(login_manager)):
    add_comment(content, article_id, user.id)
    return {"status": "success", "message": "Comment added successfully"}

@router.get("/create")
def create_article(request : Request, user: UserSchema = Depends(login_manager)):
    return templates.TemplateResponse("/create_article.html", context = {"request" : request, "user" : user})

@router.post("/create")
def create_article( title: str = Form(...), content: str = Form(...), theme: str = Form(...), user: UserSchema = Depends(login_manager)):
    
    article = ArticleSchema(id = str(uuid4()),author_username= user.username, title=title, date = datetime.now().date(), content=content , theme=theme)
    service.add_article(article)
    # return RedirectResponse(url="/articles/homepage/user_themes/data", status_code=status.HTTP_303_SEE_OTHER)
    return RedirectResponse(url="/articles/create", status_code=302)


@router.get("/edit/{article_id}")
def edit_article(request : Request, article_id: str, user: UserSchema = Depends(login_manager)):
    article = service.get_article_by_id(article_id)
    return templates.TemplateResponse("/edit_article.html", context = {"request" : request,"id": article.id ,"title" : article.title,"content": article.content ,"user" : user})

@router.post("/edit/{article_id}")
def edit_article( article_id: str, title: str = Form(...), content: str = Form(...), user: UserSchema = Depends(login_manager)):
    service.update_article(article_id, title, content)
    return RedirectResponse(url="/articles/my_articles", status_code=302)

# @router.get("/delete/{article_id}")
# def delete_article(request : Request, article_id: str, user: UserSchema = Depends(login_manager)):
#     service.delete_article(article_id)
#     return templates.TemplateResponse("/delete_article.html", context = {"request" : request, "article_id" : article_id, "user" : user})

@router.post("/delete/{article_id}")
def delete_article( article_id: str, user: UserSchema = Depends(login_manager)):
    service.delete_article(article_id)
    return RedirectResponse(url="/articles/my_articles", status_code=302)


@router.get("/my_articles")
def get_my_articles(request : Request, user: UserSchema = Depends(login_manager)):
    articles = service.get_all_articles_by_author(user)
   
    def compare_by_date(article : Article):
        # Convertir la date de l'article en objet datetime pour la comparaison
        article_date = article.date
        return article_date

    # Trier les articles par date dans l'ordre descendant en utilisant la fonction de comparaison
   
    sorted_articles = sorted(articles, key=compare_by_date, reverse=True)
    comments = {}
    for article in articles:
        comments[article.id] = get_comments_by_article(article.id)
    return templates.TemplateResponse("/my_articles.html", context = {"request" : request, "articles" : articles, "user" : user})

@router.get("/search")
def search_articles(request : Request, user: UserSchema = Depends(login_manager)):
    return templates.TemplateResponse("/search_articles.html", context = {"request" : request, "user" : user})

# @router.post("/search")
# def search_articles(request : Request, title: str = Form(...), user: UserSchema = Depends(login_manager)):
#     articles = service.get_articles_by_title(date) or 
#     return templates.TemplateResponse("/search_articles.html", context = {"request" : request, "articles" : articles, "user" : user})

@router.post("/like/{article_id}")
def like_article(article_id :str):
    service.like_article(article_id)
    return RedirectResponse(status_code=302)

@router.post("/unlike/{article_id}")
def like_article(article_id :str):
    service.unlike_article(article_id)
    return RedirectResponse(status_code=302)

@router.post("/dislike/{article_id}")
def dislike_article(article_id :str):
    service.like_article(article_id)
    return RedirectResponse(status_code=302)

@router.post("/undislike/{article_id}")
def undislike_article(article_id :str):
    service.unlike_article(article_id)
    return RedirectResponse(status_code=302)


@router.get("/get_like_count/{article_id}")
async def get_like_count(article_id: str):
    like_count = service.get_like_count(article_id)
    return PlainTextResponse(str(like_count))


@router.get("/get_dislike_count/{article_id}")
async def get_dislike_count(article_id: str):
    dislike_count = service.get_dislike_count(article_id)
    return PlainTextResponse(str(dislike_count))
