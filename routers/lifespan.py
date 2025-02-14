from contextlib import asynccontextmanager
from sqlalchemy.orm.session import Session
from fastapi import APIRouter,FastAPI,Depends
from database.db import session_local
from database.dataschema import Admins
import asyncio


async def start_24h(db:Session):
    while True:
        item = db.query(Admins).where(Admins.id == 1).update({
            "is_manager" : True
        })
        db.commit()
        await asyncio.sleep(10)




@asynccontextmanager
async def lifespan(app: FastAPI):
    session = session_local()
    await start_24h(session)
    yield
    session.close()



router = APIRouter(lifespan=lifespan)