from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from fastapi import FastAPI
from .config import Settings
from .models import Cocktail
from .routes import cocktail_router

app = FastAPI()



@app.on_event("startup")
async def app_init():
    client = AsyncIOMotorClient(Settings().mongodb_url)
    await init_beanie(client.get_database(name="beanie"), document_models=[Cocktail])
    app.include_router(cocktail_router, prefix="/v1")
