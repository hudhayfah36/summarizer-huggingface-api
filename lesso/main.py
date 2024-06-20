from fastapi import FastAPI
from transformers import pipeline 
from pydantic import BaseModel

class SummaryM(BaseModel):
    text_data : str
    max_l :int
    min_l : int

app = FastAPI()


@app.get("/")
def show():
    return "helllo "

@app.post("/meow")
async def giveresponse(userdata:SummaryM):
    summarizer = pipeline("summarization")
    summary = summarizer(userdata.text_data,max_length=userdata.max_l,min_length=userdata.min_l,do_sample = True)
    return summary