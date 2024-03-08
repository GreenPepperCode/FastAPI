from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Joke(BaseModel):
    setup: str
    punchline: str

class Quote(BaseModel):
    author: str
    text: str

@app.get("/", tags=["Home"])
def read_root():
    return {"Hello": "World"}

@app.get("/hello/{name}", response_description="Personalized greeting", tags=["Greetings"])
def hello(name: str):
    """
    Say hello to a specific person.

    Parameters:
    - name: The name of the person to greet.
    """
    return {"message": f"Hello, {name}!"}

@app.get("/jokes", response_model=List[Joke], response_description="A list of jokes", tags=["Humor"])
def jokes():
    """
    Get a list of jokes.
    """
    jokes = [
        {"setup": "Why did the chicken cross the road?", "punchline": "To get to the other side!"},
        {"setup": "Why don't scientists trust atoms?", "punchline": "Because they make up everything!"},
        {"setup": "How do you organize a space party?", "punchline": "You planet!"}
    ]
    return jokes

@app.get("/quotes", response_model=List[Quote], response_description="A list of inspiring quotes", tags=["Inspiration"])
def quotes():
    """
    Get a list of inspiring quotes.
    """
    quotes = [
        {"author": "Steve Jobs", "text": "The only way to do great work is to love what you do."},
        {"author": "Theodore Roosevelt", "text": "Believe you can and you're halfway there."},
        {"author": "Eleanor Roosevelt", "text": "The future belongs to those who believe in the beauty of their dreams."}
    ]
    return quotes
