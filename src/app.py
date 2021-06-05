from fastapi import FastAPI
from routers import abstractive_router, extractive_router

app = FastAPI(title="Abstractive and Extractive Text Summarizer")

app.include_router(extractive_router.router)
app.include_router(abstractive_router.router)
