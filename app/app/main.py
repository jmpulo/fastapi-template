from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from core.config import settings
from api.api_v1.api import api_router


app = FastAPI(
    title=settings.APP_NAME, openapi_url=f"{settings.API_V1_URI}/openapi.json"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_URI)