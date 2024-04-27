from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles   
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI,Request,status
from App.Routes.articles import router as article_router
from App.Routes.users import router as user_router
from App.database import create_database, clear_database



templates = Jinja2Templates(directory="\TP4\Librairie\Templates")


app = FastAPI(title="My bookstore")
app.include_router(article_router)
app.include_router(user_router)

@app.get("/")
def route(request: Request):
    return RedirectResponse("./users/login", status_code= status.HTTP_303_SEE_OTHER)

app.mount("/static", StaticFiles(directory="Static"), name="static")

@app.on_event('startup')
def on_startup():
    print("Server started.")
    create_database()


def on_shutdown():
    print("Bye bye!")
    clear_database()
