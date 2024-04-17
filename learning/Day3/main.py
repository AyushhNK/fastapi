from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Student(BaseModel):
	name:str
	age:int

@app.post("/student")
def student(student:Student):
	return student
