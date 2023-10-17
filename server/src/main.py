import uvicorn
from fastapi import FastAPI

from src.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"/{settings.API_V1_STR}/openapi.json"
)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=1324)
