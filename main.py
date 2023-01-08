from fastapi import FastAPI

from example import router as example_router

app = FastAPI()

app.include_router(example_router)
