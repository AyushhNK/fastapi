from fastapi import FastAPI
import requests

app=FastAPI()

@app.get('/weather/{city}')
async def index(city:str):
	api_url = f'https://api.api-ninjas.com/v1/weather?city={city}'.format(city)
	response = requests.get(api_url, headers={'X-Api-Key': '5qaxvKD2gEZ53oGe/AuzsQ==Z27MXTAXLCECGFz7'})
	if response.status_code == requests.codes.ok:
	    return {"data":response.text}
	else:
	    return {
	    "error":"there was some problem"
	    }

