from typing import Annotated
from fastapi import APIRouter, HTTPException, status, Depends, Form
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.responses import JSONResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates


from Templates import *
from App.login_manager import *
from App.Services import users as userService
from App.Schemas import 

templates = Jinja2Templates(directory="\Templates")
router = APIRouter(prefix="/users")

