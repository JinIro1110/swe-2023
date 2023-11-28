from fastapi import FastAPI
from models import ReviewRequest, ReviewResponse
from keyword_extraction.keyword_model import keyword_extraction_model
from app import aasdf

app = FastAPI()

@app.post("/process_review/", response_model=ReviewResponse)
def process_review(review: ReviewRequest):
    json_file = aasdf()

    return json_file
