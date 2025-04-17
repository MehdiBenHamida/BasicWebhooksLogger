from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .database import Base, engine
from .routes import api, web

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api.router)
app.include_router(web.router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
