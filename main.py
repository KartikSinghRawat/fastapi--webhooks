from fastapi import FastAPI , HTTPException
from pydantic import BaseModel


class Item(BaseModel):
    text : str =  None
    is_done : bool = False

app= FastAPI()

items = []
# default route
@app.get("/")
def root():
    return {"hello" : "world"}

#making functional routes
@app.post("/items")
def createitem(item :Item):
    items.append(item)
    return items

@app.get("/items/{item_id}" , response_model=Item)
def getitem(item_id : int)  -> Item:
    if (item_id < len(items)):
        item = items[item_id] # if id is out of bound default error is internal server error 
        return item
    else :
        raise HTTPException(status_code=404 , detail= f"Item at {item_id} not found !") # this library is very helpful for exception handling in api's
