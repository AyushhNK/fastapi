from fastapi import FastAPI
from enum import Enum

app=FastAPI()


# to print hello world in fast api
@app.get("/")
async def root():
	return {"message":"hello world"}

# get request with path parameter
@app.get("/items/{item_id}")
async def item(item_id):
	return {"message":item_id}


# creating a enum
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/item/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]