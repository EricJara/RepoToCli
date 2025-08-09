import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/familia")
def get_familia():
    rows = ["Amin", "Marce", "Miranda"]
    return rows


@app.get("/superheroesDC")
def get_superheroesdc():
    rows = ["Superman", "Batman", "Flash", "Linterna Verde", "Mujer maravilla", "Aquaman", "Shazam", "Cyborg"]
    
    return rows


@app.get("/cursosPlatzi")
def get_cursosplatzi():
    rows = ["Azure", "Bash", "Python", "GitHub", "Power BI", "Cloud", "AWS", "Terraform"]
    
    return rows


@app.get("/cursosUdemy")
def get_cursoudemy():
    rows = ["Azure", "AWS", "WEB_SCRAPING"]
    
    return rows