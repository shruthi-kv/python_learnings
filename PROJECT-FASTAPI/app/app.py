from fastapi import FastAPI, HTTPException
from app.schema import PostCreate


app = FastAPI()

posts = {
    1: {
        "title": "Atomic Habits",
        "content": "A book about building good habits and breaking bad ones."
    },
    2: {
        "title": "The Alchemist",
        "content": "A young shepherd travels in search of his dreams and discovers the meaning of life."
    },
    3: {
        "title": "Rich Dad Poor Dad",
        "content": "A book that explains the importance of financial knowledge and money management."
    },
    4: {
        "title": "The Power of Now",
        "content": "A guide to living in the present moment and finding inner peace."
    },
    5: {
        "title": "Ikigai",
        "content": "A book about finding purpose and living a happy and meaningful life."
    },
    6: {
        "title": "The Psychology of Money",
        "content": "Explores how emotions and behaviour influence our financial decisions."
    },
    7: {
        "title": "Think Like a Monk",
        "content": "Teaches how to develop a calm mind and live with purpose."
    },
    8: {
        "title": "Wings of Fire",
        "content": "The autobiography of A.P.J. Abdul Kalam, sharing his journey and achievements."
    },
    9: {
        "title": "The Secret",
        "content": "Explains how positive thinking and belief can influence our lives."
    },
    10: {
        "title": "Deep Work",
        "content": "A guide to improving focus and producing meaningful work without distractions."
    }
}

@app.get("/posts")
def get_all_posts(limit :int = None):
    if limit:
        return list(posts.values())[:limit]
    return posts

@app.get("/post/{id}")
def get_post(id:int):
    if id not in posts:
        raise HTTPException(status_code = 404, detail ="not found")
    return posts.get(id)

@app.post("/posts")
def post_posts(post : PostCreate):
    newPost = {"title" : post.title , "content" : post.content}
    posts[max(posts.keys()) + 1] = newPost
    return newPost