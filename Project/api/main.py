from fastapi import FastAPI
from models import ReviewRequest, ReviewResponse
from keyword_extraction.keyword_model import keyword_extraction_model

app = FastAPI()

@app.post("/process_review/", response_model=ReviewResponse)
def process_review(review: ReviewRequest):
    preprocessed_review = preprocess_review(review.text)
    sentiment_score = sentiment_analysis_model(preprocessed_review)
    keywords = keyword_extraction_model(preprocessed_review)
    
    response = {
        "sentiment_score": sentiment_score,
        "keywords": keywords
    }

    return response
