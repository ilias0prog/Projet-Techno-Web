from typing import Annotated
from fastapi import APIRouter, HTTPException, status, Depends, Form
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.responses import JSONResponse
from Templates import *
from app.login_manager import *
import app.services.users as service
from app.schemas.user import UserSchema
from fastapi.templating import Jinja2Templates
from fastapi import Request



templates = Jinja2Templates(directory="Librairie\Templates")
router = APIRouter(prefix="/users")
@router.get("/login")
def login_form(request: Request):
    return templates.TemplateResponse("/login.html", {"request": request})
"""
@router.post("/login")
def login_route( username: Annotated[str, Form()], password: Annotated[str,Form()]):
    
    user = service.get_user_by_username(username)
    if user is not None:
        if user.password != password:
            return HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="incorrect password.")
        
        access_token = login_manager.create_access_token(
            data={'sub': user.id}
        )
        response = RedirectResponse(url="/articles/homepage", status_code=302)
        response.set_cookie(
            key=login_manager.cookie_name,
            value=access_token,
            httponly=True
        )
        return response
"""


@router.post("/login")
def login_route( username: Annotated[str, Form()], password: Annotated[str,Form()]):
    
    user = service.get_user_by_username(username)
    if user is not None:
        if user.password != password:
            return HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="incorrect password.")
        
        access_token = login_manager.create_access_token(
            data={'sub': user.id}
        )
        response = RedirectResponse(url="/articles/homepage/user_themes/data", status_code=302)
        response.set_cookie(
            key=login_manager.cookie_name,
            value=access_token,
            httponly=True
        )
        return response




@router.get("/logout/")
def logout_form(request: Request):
    return templates.TemplateResponse("/logout.html", {"request": request })

@router.post('/logout/')
def logout_route():
    response = RedirectResponse(url="/users/login", status_code=302)
    response.delete_cookie(
        key=login_manager.cookie_name,
        httponly=True
    )
  
    return response


@router.get("/my_profile")
def current_user_route(request : Request, user: UserSchema = Depends(login_manager)):
    
    return templates.TemplateResponse("user.html", context={"request": request,"id": user.id, "username": user.username, "firstname": user.firstname, "name": user.name, "email": user.email, "interests" : user.interests.split(' ')})





@router.get("/register")
def register_form(request: Request):
    return templates.TemplateResponse("/register.html", context={"request": request})

@router.post("/register")
def  register_action( username:Annotated[str, Form()], firstname: Annotated[str, Form()], name:Annotated[str, Form()],email:Annotated[str, Form()], password: Annotated[str, Form()], confirm_password: Annotated[str, Form()]):
    service.register(username, firstname, name, email, password, confirm_password)
    response = RedirectResponse(url="/books/all", status_code=302)
    return  response


@router.get("/admin")
def admin_form(request: Request):
    return templates.TemplateResponse("/admin.html", context={"request": request, "users": service.get_all_users()})

@router.post("/admin")
def admin_action(id: Annotated[str, Form()]):
    service.grant_admin(id)
    response = RedirectResponse(url="/users/admin", status_code=302)
    return response

@router.get("/updateprofile/{user_id}")
def update_form(user_id : str, request: Request, user: UserSchema = Depends(login_manager)):
    user = get_user_by_id(user_id)
    return templates.TemplateResponse("/updateprofile.html", context={"request": request, "user": user})

@router.post("/updateprofile/{user_id}")
def update_action(user_id: str, username: Annotated[str, Form()], firstname: Annotated[str, Form()], name: Annotated[str, Form()], email: Annotated[str, Form()], password: Annotated[str, Form()], interests: Annotated[str, Form()]):
    service.update_user(user_id, username, firstname, name, email, password, interests)
    response = RedirectResponse(url="/users/myprofile", status_code=302)
    return response

@router.get("/delete/{user.id}")
def delete_form(request: Request, user: UserSchema):
    return templates.TemplateResponse("/delete.html", context={"request": request, "user": user})

@router.post("/delete/{user.id}")
def delete_action(id: Annotated[str, Form()]):
    service.delete_user(id)
    response = RedirectResponse(url="/users/myprofile", status_code=302)
    return response

@router.get("/edit-password")
def edit_password(request : Request ,user: UserSchema = Depends(login_manager)):
    return templates.TemplateResponse("/edit-password.html", context={"request": request, "user": user})