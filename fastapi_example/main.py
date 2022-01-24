from typing import Optional

from fastapi import FastAPI

app = FastAPI()
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


class Car(BaseModel):
    name: str
    price: int
    item: Item


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.post('/item/create')
async def create_item(item: Item):
    return {'created': item.name}


@app.options('/car/return', response_model=Car)
async def return_car():
    item = Item(name='руль', price=122)
    return Car(name='БМВ', price=1000, item=item)
