from .database import posts_collection
from .models import Post, PostUpdate
from bson import ObjectId

async def create_post(post: Post) -> dict:
    post = post.dict()
    result = await posts_collection.insert_one(post)
    post["_id"] = str(result.inserted_id)
    return post

async def get_post(post_id: str) -> dict:
    post = await posts_collection.find_one({"_id": ObjectId(post_id)})
    if post:
        post["_id"] = str(post["_id"])
    return post

async def update_post(post_id: str, data: PostUpdate) -> dict:
    data = {k: v for k, v in data.dict().items() if v is not None}
    if not data:
        return None
    await posts_collection.update_one({"_id": ObjectId(post_id)}, {"$set": data})
    post = await get_post(post_id)
    return post

async def delete_post(post_id: str) -> bool:
    result = await posts_collection.delete_one({"_id": ObjectId(post_id)})
    return result.deleted_count > 0

async def list_posts() -> list:
    posts = []
    async for post in posts_collection.find():
        post["_id"] = str(post["_id"])
        posts.append(post)
    return posts