from fastapi import FastAPI
from app.router.user import router as user_router
from app.router.auth import router as auth_router
from app.router.pet import router as pet_router
from app.router.clinic import router as clinic_router

app = FastAPI()

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(pet_router)
app.include_router(clinic_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
