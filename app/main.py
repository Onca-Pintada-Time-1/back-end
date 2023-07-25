from fastapi import FastAPI

from app.Routers import XGBRouter

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# app.include_router(router, prefix="/teste")
app.include_router(XGBRouter.router)
