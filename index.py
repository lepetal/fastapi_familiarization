from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, PositiveInt
from pprint import pprint

app = FastAPI()

templates = Jinja2Templates(directory="templates")

class Item(BaseModel):
    number1: PositiveInt
    number2: PositiveInt

@app.post("/calc/", status_code=200)
async def calculate(item: Item):
    item_dict = item.dict()
    result = {"result": item_dict['number1'] + item_dict['number2']}
    return result

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
