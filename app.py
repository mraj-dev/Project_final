from fastapi import FastAPI
from fastapi.responses import JSONResponse

from .util import *

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/get-data")
def get_data():
    content = api_request()
    response=JSONResponse(content=content )
    return response