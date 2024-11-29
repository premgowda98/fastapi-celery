from fastapi import FastAPI
from fastapi.responses import JSONResponse
from tasks import process_image
import uvicorn

app = FastAPI()

@app.get("/")
def hello_word():
    return JSONResponse(content={'message': 'Hello World'})

@app.post("/image")
def process():
    result = process_image.delay()

    return JSONResponse(content={'message': 'Processing started'})

if __name__=="__main__":
    uvicorn.run("app:app", port=5678, host="0.0.0.0")