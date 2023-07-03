from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def get_index():
    return FileResponse("templates/index.html")

@app.get("/calculate_bmi")
async def calculate_bmi(height:str, weight:str):
    bmi = int(weight) / (int(height) ** 2)
    category = get_bmi_category(bmi)
    return {"bmi":bmi,"category":category} 

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"
