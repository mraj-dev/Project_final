from typing import *
from fastapi import FastAPI
from .util import *

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/get-data")
def get_data():
    return api_request()