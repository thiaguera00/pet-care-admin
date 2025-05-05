from fastapi import FastAPI
from app.router.user import router as user_router
from app.router.auth import router as auth_router

app = FastAPI()

app.include_router(user_router)
app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
