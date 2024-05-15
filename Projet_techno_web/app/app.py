from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles   
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI,Request,status
from app.Routes.articles import router as article_router
from app.Routes.users import router as user_router
from app.database import *



templates = Jinja2Templates(directory="\Projet_techno_web\Templates")


app = FastAPI(title="My bookstore")
app.include_router(article_router)
app.include_router(user_router)

@app.get("/")
def route(request: Request):
    return RedirectResponse("./users/login", status_code= status.HTTP_303_SEE_OTHER)

app.mount("/static", StaticFiles(directory="Projet_techno_web/Static"), name="static")

@app.on_event('startup')
def on_startup():
    print("Server started.")
    create_database()


def on_shutdown():
    print("Bye bye!")
    clear_database()
