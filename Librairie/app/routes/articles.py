from typing import Annotated
from fastapi import APIRouter, HTTPException, status, Depends, Form
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.responses import JSONResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates
from app.schemas import *
from Templates import *
from app.login_manager import *
from app.services import articles as service
from app.services.users import get_user_by_id
from app.schemas.user import UserSchema



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
