import uvicorn
from fastapi import FastAPI

from app.db import db
from app.rest import users

app = FastAPI(title="FastAPI")

app.include_router(users.router, prefix='/api/users')


@app.on_event("startup")
async def startup():
    await db.connect_to_database(path="YOUR MONGODB CONNECTION STRING")


@app.on_event("shutdown")
async def shutdown():
    await db.close_database_connection()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
