# illustration_only/fastapi_example.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Event(BaseModel):
    title: str
    capacity: int

@app.get("/events/")
async def list_events() -> list[Event]:
    # You bring the database layer, auth, and admin
    return [Event(title="Community Meetup", capacity=50)]
