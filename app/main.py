from fastapi import FastAPI

from app.Routers import XGBRouter
from app.Routers import scattersRouter

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(XGBRouter.router)
app.include_router(scattersRouter.router)
