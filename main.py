from fastapi import FastAPI, Request

from routes.user import user


app = FastAPI()

app.include_router(user)


