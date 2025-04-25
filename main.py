from fastapi import FastAPI, Request
from enum import Enum


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/count")
def count(request: Request):
    data = request.json()
    print(data)
    return {"message": "Hello World2"}

@app.get("/items/{item_id}")
async def items(item_id:str):
    return {"message": f"Item ID: {item_id}"}

class FoodItems(str,Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"

@app.get("/food/{food_item}")
async def food_item(food_item: FoodItems):
    if food_item == FoodItems.fruits:
        return ["Apple","Banana","Orange"]
    elif food_item == FoodItems.vegetables:
        return ["Carrot","Potato","Onion"]
    else:
        return ["Milk","Cheese","Yogurt"]
    
    
    