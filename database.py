import motor.motor_asyncio
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL:str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "school_blog"

settings=Settings()
client=motor.motor_asyncio.AsyncIOMotorClient(settings.DATABASE_URL)
database=client[settings.DATABASE_NAME]
posts_collection=database["posts"]