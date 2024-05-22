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
from app.schemas.user import UserSchema
from app.services.comments import *



templates = Jinja2Templates(directory="Librairie\Templates")
router = APIRouter(prefix="/articles", tags=["articles"])


@router.get("/homepage")
def get_feed(request : Request, user: UserSchema = Depends(login_manager)):
    # Fetch connected user info with cookie 
    themes = user.interests.split(' ')
    articles = service.get_all_articles_by_themes(themes)

    print(themes)
    print(service.get_all_articles_by_themes(themes))
    return templates.TemplateResponse("/homepage.html", context = {"request" : request, "articles" : articles, "user" : user})

@router.post("/load-comments/")
async def load_comments(article_id: int):
    comments = get_comments_by_article(article_id)
    return {"comments": comments}

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

@router.post("delete/{article_id}")
def delete_article(request : Request, article_id: str, user: UserSchema = Depends(login_manager)):
    service.delete_article(article_id)
    return RedirectResponse(url="/articles/homepage")


