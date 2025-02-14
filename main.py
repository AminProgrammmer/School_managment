from fastapi import FastAPI
from authentication import authentication
from routers import admins,lifespan

from database.db import base,engine

app = FastAPI()
app.include_router(authentication.router)

app.include_router(admins.router)
app.include_router(lifespan.router)

base.metadata.create_all(engine)


@app.get("/")
def Home():
    return {"hello":"hello"}