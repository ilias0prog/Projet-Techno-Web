import uvicorn


if __name__ == '__main__':
    uvicorn.run("App.app:app", log_level="info", port=8000)