from fastapi import FastAPI

app=FastAPI()

@app.get("/item/{item_id}")
async def home(item_id:int):
	return {"message":item_id}