# main.py
from functools import lru_cache
from fastapi import FastAPI
from config import Settings
from routers import events

@lru_cache()
def get_settings():
    return Settings()

def get_app() -> FastAPI:
    app = FastAPI(**get_settings().fastapi_kwargs())
    return app

app = get_app()

app.include_router(events.router)
