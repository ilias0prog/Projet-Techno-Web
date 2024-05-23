from typing import Annotated
from fastapi import APIRouter, HTTPException, status, Depends, Form
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.responses import JSONResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates
from app.schemas.article import *
from Templates import *
from app.login_manager import *
from app.services import articles as service
from app.services.users import get_user_by_id
from app.services.comments import *
from app.schemas.user import UserSchema
from app.schemas.comment import CommentSchema
from app.services.comments import *



templates = Jinja2Templates(directory="Librairie\Templates")
router = APIRouter(prefix="/articles", tags=["articles"])


@router.get("/homepage")
def get_feed(request : Request, user: UserSchema = Depends(login_manager)):
    # Fetch connected user info with cookie 
    themes = user.interests.split(' ')
    articles = service.get_all_articles_by_themes(themes)

    # comments = []
    # for article in articles:
    #     for comment in get_comments_by_article(article.id):
    #         comments.append[comment]
    comments = {}
    for article in articles:
        comments[article.id] = get_comments_by_article(article.id)

    return templates.TemplateResponse("/homepage.html", context = {"request" : request, "articles" : articles, "user" : user, "comments" : comments})

@router.post("/load_comments")
async def load_comments(article_id: int):
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
def create_article(request : Request, title: str = Form(...), content: str = Form(...), theme: str = Form(...), user: UserSchema = Depends(login_manager)):
    article = ArticleSchema(title=title, content=content, theme=theme, author=user.username)
    service.add_article(article)
    return RedirectResponse(url="/articles/homepage")

@router.get("/edit/{article_id}")
def edit_article(request : Request, article_id: str, user: UserSchema = Depends(login_manager)):
    article = service.get_article_by_id(article_id)
    return templates.TemplateResponse("/edit_article.html", context = {"request" : request, "article" : article, "user" : user})

@router.post("/edit/{article_id}")
def edit_article(request : Request, article_id: str, title: str = Form(...), content: str = Form(...), theme: str = Form(...), user: UserSchema = Depends(login_manager)):
    article = ArticleSchema(title=title, content=content, theme=theme, author=user.username)
    service.update_article(article_id, article)
    return RedirectResponse(url="/articles/homepage")

@router.get("/delete/{article_id}")
def delete_article(request : Request, article_id: str, user: UserSchema = Depends(login_manager)):
    service.delete_article(article_id)
    return RedirectResponse(url="/articles/homepage")

@router.post("/delete/{article_id}")
def delete_article(request : Request, article_id: str, user: UserSchema = Depends(login_manager)):
    service.delete_article(article_id)
    return RedirectResponse(url="/articles/homepage")


@router.get("/myarticles")
def get_my_articles(request : Request, user: UserSchema = Depends(login_manager)):
    articles = service.get_all_articles_by_author(user.username)
    return templates.TemplateResponse("/my_articles.html", context = {"request" : request, "articles" : articles, "user" : user})

@router.get("/search")
def search_articles(request : Request, user: UserSchema = Depends(login_manager)):
    return templates.TemplateResponse("/search_articles.html", context = {"request" : request, "user" : user})

@router.post("/search")
def search_articles(request : Request, title: str = Form(...), user: UserSchema = Depends(login_manager)):
    articles = service.get_articles_by_title(date) or 
    return templates.TemplateResponse("/search_articles.html", context = {"request" : request, "articles" : articles, "user" : user})
