import uvicorn
from fastapi import FastAPI
from routers import user_public_router, user_internal_router

app = FastAPI()

app.include_router(user_public_router, prefix="/users")
app.include_router(user_internal_router, prefix="/internal/users")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8008, reload=True)
