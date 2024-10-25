from fastapi import FastAPI, HTTPException
from typing import List
from .models import Post, PostUpdate
from .crud import create_post, get_post, update_post, delete_post, list_posts

app = FastAPI()

@app.post("/posts", response_model=Post)
async def create_new_post(post: Post):
    post = await create_post(post)
    return post

@app.get("/posts", response_model=List[Post])
async def get_all_posts():
    posts = await list_posts()
    return posts

@app.get("/posts/{post_id}", response_model=Post)
async def get_post_by_id(post_id: str):
    post = await get_post(post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.put("/posts/{post_id}", response_model=Post)
async def update_existing_post(post_id: str, post: PostUpdate):
    updated_post = await update_post(post_id, post)
    if updated_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return updated_post

@app.delete("/posts/{post_id}")
async def delete_post_by_id(post_id: str):
    deleted = await delete_post(post_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted successfully"}