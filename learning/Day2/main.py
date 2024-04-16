from fastapi import FastAPI
from enum import Enum
from typing import Optional

app=FastAPI()


@app.get('/users')
def get_user():
	return {"message":"hello user"}

@app.get('/users/me')
def get_current_user():
	return {"message":"It is the current user"}

@app.get('/users/{user_id}')
async def get_user_with_id(user_id:str):
	return {'message':user_id}

class FoodEnum(str,Enum):
	fruits="fruits"
	vegetables="vegetables"
	dairy="dairy"

@app.get('/food/{food_name}')
async def get_food(food_name:FoodEnum):
	if food_name=='vegetables':
		return {"food_name":food_name,"message":"you are eating healthy vegetables"}
	elif food_name=='fruits':
		return {"food_name":food_name,"message":"you are eating healthy vegetables"}
	return {"food_name":food_name,"message":"you are eating healthy dairy"}


fake_db=[{"items":"foo"},{"items":"bar"},{"items":"nam"}]

@app.get('/items')
async def list_items(skip:int=0,limit:int=5):
	return  fake_db[skip:skip+limit]


@app.get('/items/{items_id}')
async def get_items(items_id,q:str|None=None):
	if q:
		return {"items_id":items_id,"q":q}
	return {"items_id":items_id}