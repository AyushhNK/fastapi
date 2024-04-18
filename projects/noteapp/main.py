from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from pymongo import MongoClient

app=FastAPI()
templates=Jinja2Templates(directory='templates')

class Note(BaseModel):
	title:str
	desc:str

url='mongodb+srv://ayush:aTyzN1DVGOEy134y@cluster6.nvxaegs.mongodb.net'
conn=MongoClient(url)

@app.get('/',response_class=HTMLResponse)
async def get_items(request:Request):
	docs=conn.Note.note.find({})
	newdocs=[]
	for doc in docs:
		newdocs.append({
			'id':doc['_id'],
			'title':doc['title'],
			'desc':doc['desc']
			})
	return templates.TemplateResponse('index.html',{'request':request,"newdocs":newdocs})
@app.post('/')
async def post_note(request:Request):
	form=await request.form()
	note=conn.Note.note.insert_one(dict(form))
	return {"message":"success"}
	# return templates.TemplateResponse('index.html',{'request':request})