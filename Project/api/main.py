from fastapi import FastAPI, HTTPException
import subprocess
import os
import json

app = FastAPI()
print(os.getcwd())

# Activate conda environment

# Change directory

subprocess.run(["conda", "activate", "pknu"])


@app.post("/getJson/{itemId}")
def process_review(itemId: int):
    try:
        os.chdir('C:/Users/user/Desktop/swe-pknu/swe-2023/Project/sentiment')
        subprocess.run(["python", "app.py", f"{itemId}"])

        # Open and read the content of the "result.json" file
        os.chdir('C:/Users/user/Desktop/swe-pknu/swe-2023/Project/api')
        with open("result.json", "r", encoding="utf-8") as f:
            result_content = json.load(f)

        # Return the content
        return result_content
    except Exception as e:
        print(f"Error in process_review: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
    
@app.post("/")
def hello():
    print('hello')
    
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=1004)

