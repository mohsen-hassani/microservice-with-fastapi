import uvicorn
from fastapi import FastAPI
from routers import feedback_public_router

app = FastAPI()

app.include_router(feedback_public_router, prefix="/feedbacks")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8009, reload=True)
