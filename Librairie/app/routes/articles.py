from typing import Annotated
from fastapi import APIRouter, HTTPException, status, Depends, Form
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.responses import JSONResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates
from app.schemas import *
from Templates import *
from app.login_manager import *
from app.services import articles as articleService


templates = Jinja2Templates(directory="Librairie\Templates")
router = APIRouter(prefix="/articles", tags=["articles"])



