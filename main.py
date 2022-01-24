#uvicorn main:app --reload --host 0.0.0.0 --port 5000
#mongodb://localhost:27017
#docker run --rm --name mongo -p 27017:27017 -d mongo

#https://testdriven.io/blog/fastapi-mongo/

from fastapi import FastAPI
from routes.student import router as StudentRouter

app = FastAPI()

app.include_router(StudentRouter, tags=["Student"], prefix="/student")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}