from fastapi import FastAPI

from routers import admins

from database.db import base,engine

app = FastAPI()

app.include_router(admins.router)

base.metadata.create_all(engine)




@app.get("/")
def Home():
    return {"hello":"hello"}