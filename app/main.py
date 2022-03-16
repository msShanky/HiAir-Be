from fastapi import FastAPI
from app.routers import candidate, request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(candidate.router)
app.include_router(request.router)


@app.get("/")
async def root():
    return {"message": "The application is healthy!"}
