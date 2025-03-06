from fastapi import FastAPI
from authentication import authentication
from routers import admins,lifespan,classes,major,book,student,grade

from database.db import base,engine

app = FastAPI()
app.include_router(lifespan.router)
app.include_router(authentication.router)

app.include_router(admins.router)
app.include_router(classes.router)
app.include_router(grade.router)

app.include_router(major.router)
app.include_router(book.router)
app.include_router(student.router)

base.metadata.create_all(engine)


@app.get("/")
def Home():
    return {"hello":"hello"}