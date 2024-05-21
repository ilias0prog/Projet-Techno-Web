from fastapi import FastAPI,Request,status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from app.routes.articles import router as article_router
from app.routes.users import router as user_router
from starlette.staticfiles import StaticFiles   
from fastapi.staticfiles import StaticFiles
from app.database import *

templates = Jinja2Templates(directory="Librairie\Templates")


app = FastAPI(title="Twitter")

app.include_router(user_router)
app.include_router(article_router)

@app.get("/")
def route(request: Request):
    return RedirectResponse("./users/login", status_code= status.HTTP_303_SEE_OTHER)

app.mount("/static", StaticFiles(directory="Librairie/static"), name="static")

@app.on_event('startup')
def on_startup():
    print("Server started.")
    create_database()
    fill_users_db()
    fill_articles_db()



def on_shutdown():
    print("Bye bye!")
    clear_database()
