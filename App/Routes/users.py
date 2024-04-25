from typing import Annotated
from fastapi import APIRouter, HTTPException, status, Depends, Form
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.responses import JSONResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates


from Templates import *
from App.login_manager import *
from App.Services import users as userService
from App.Schemas.user import UserSchema

templates = Jinja2Templates(directory="\Templates")
router = APIRouter(prefix="/users")


@router.get("/login")
def login_page(request: Request):
        return templates.TemplateResponse("/login.html", {"request": request})


@router.post("/login")
def login_route(username: Annotated[str, Form()], password: Annotated[str, Form()]):
        user = service.get_user_by_username(username)
        if user is not None:
                if user.blocked:
                        return HTTPException(
                                status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="User is blocked.")
                        
        if user is None or user.password != password:
            return HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="incorrect username or password.")