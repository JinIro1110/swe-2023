from fastapi import FastAPI
import sys
import os
os.chdir('../sentiment')
import logging

from app import getJson

app = FastAPI()

logging.basicConfig(level=logging.DEBUG)
@app.post("/getJson/{itemId}")
def process_review(itemId: int):
    try:
        json_result = getJson(itemId)
        return json_result
    except Exception as e:
        # Log any exception that occurs
        logging.error(f"An error occurred in process_review: {str(e)}")
        return {'error': 'Internal Server Error'}
