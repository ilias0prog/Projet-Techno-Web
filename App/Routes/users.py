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

# Login routes :
@router.get("/login")
def login_page(request: Request):
        return templates.TemplateResponse("/login.html", {"request": request})

@router.post("/login")
def login_route(username: Annotated[str, Form()], password: Annotated[str, Form()]):
        user = userService.get_user_by_username(username)
        if user is not None:
                if user.blocked:
                        return HTTPException(
                                status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="User is blocked.")
                        
        if user is None or user.password != password:
            return HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="incorrect username or password.")
            
            
@router.get("/logout/")
def logout_form(request: Request):
    return templates.TemplateResponse("/logout.html", {"request": request })

@router.post("logout")
def lougout_route():
        response = RedirectResponse(url="/users/login", status_code=302)
        response.delete_cookie(
                key = login_manager.cookie_name,
                httponly=True)
        return response

@router.get("/me")
def current_user_page(request : Request, user: UserSchema = Depends(login_manager)):
    return templates.TemplateResponse("my_profile.html", context={"request": request,"user": user})

@router.get("/thisuser")
def this_user_page(request : Request, this_user : UserSchema):
    return templates.TemplateResponse("this_user.html", context={"request": request, "this_user": this_user})

@router.get("/register")
def register_page(request: Request):
    return templates.TemplateResponse("/register.html", context={"request": request})


@router.post("/register")
def register_route( username:Annotated[str, Form()], firstname: Annotated[str, Form()], name:Annotated[str, Form()],email:Annotated[str, Form()], password: Annotated[str, Form()], confirm_password: Annotated[str, Form()]):
    userService.register(username, firstname, name, email, password, confirm_password)
    response = RedirectResponse(url="/books/all", status_code=302)
    return  response

