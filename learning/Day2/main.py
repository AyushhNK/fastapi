from fastapi import FastAPI
from enum import Enum

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
