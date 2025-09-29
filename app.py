from fastapi import FastAPI,Request,Response
import pickle
import pandas as pd
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

#Templates
templates = Jinja2Templates(directory="templates")

with open("final_project.pkl", "rb") as f:
    saved_data = pickle.load(f)

model=saved_data["model"]
gender_encoder=saved_data["gender_encoder"]
part_time_encoder=saved_data["part_time_encoder"]
extra_encoder=saved_data["extra_encoder"]
ord_diet=saved_data["ord_diet"]
ord_parent=saved_data["ord_parent"]
ord_internet=saved_data["ord_internet"]

class StudentFeatures(BaseModel):
    age: int
    gender:str
    study_hours_per_day:float
    social_media_hours:float
    netflix_hours:float
    part_time_job:str
    attendance_percentage:float
    sleep_hours:float
    diet_quality:str
    exercise_frequency:int
    parental_education_level:str
    internet_quality:str
    mental_health_rating:int
    extracurricular_participation:str


@app.get("/",response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html",{"request": request})

@app.post("/predict")
async def predict(features: StudentFeatures):
    input_data = pd.DataFrame([features.model_dump()])

    input_data["gender"] = gender_encoder.transform(input_data["gender"])
    input_data["part_time_job"] = part_time_encoder.transform(input_data["part_time_job"])
    input_data["extracurricular_participation"] = extra_encoder.transform(input_data["extracurricular_participation"])

    input_data["diet_quality"] = ord_diet.transform(input_data[["diet_quality"]])
    input_data["parental_education_level"] = ord_parent.transform(input_data[["parental_education_level"]])
    input_data["internet_quality"] = ord_internet.transform(input_data[["internet_quality"]])

    prediction = model.predict(input_data)

    return {"prediction": float(prediction[0])}  # numpy tipini float'a çevir