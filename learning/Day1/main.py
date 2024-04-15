from fastapi import FastAPI

app=FastAPI()

@app.get("/",description="this is the get route")
def get():
    return {"message":"hello form the get route"}


@app.post("/")
def post():
    return {"message":"hello form the post route"}


@app.put("/")
def put():
    return {"message":"hello form the put route"}