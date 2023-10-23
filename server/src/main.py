import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse

from src.api.v1.routers import router as api_router_v1
from src.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)

app.include_router(api_router_v1, prefix=settings.API_V1_STR)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=1324)
