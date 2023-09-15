from os import path, getenv
from uvicorn import Config, Server
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.routing import APIRouter
async def index():
    return {}

from .extensions import *

def create_app():
    app = FastAPI(debug=True, title="Fastinni")

    # -----------------------
    # | FASTAPI MIDDLEWARES |
    # -----------------------
    app.add_middleware(AsyncExitStackMiddleware)
    app.add_middleware(CORSMiddleware, allow_origins=getenv("FASTAPI_CORS_ALLOWED_ORIGINS", "127.0.0.1:5000").split(";"), 
                        allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
    app.add_middleware(GZipMiddleware, minimum_size=int(getenv("FASTAPI_GZIP+MINIMUM_SIZE", "1000")))
    #app.add_middleware(TrustedHostMiddleware, allowed_hosts=TRUSTED_HOSTS) # uncomment these lines if you want that extra step in security
    # app.add_middleware(HTTPSRedirectMiddleware)

    # ----------------
    # - APP ASSEMBLY |
    # ----------------
    app.mount(path='/', app=StaticFiles(directory='fastinni/pages', html=True), name='Pages') # type: ignore
    
    api = APIRouter(prefix="/api")
    api.add_api_route('/', index)
    #from . import api
    app.include_router(api) # type: ignore
    return app
