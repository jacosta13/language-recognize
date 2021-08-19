from fastapi import FastAPI
from fastapi.responses import JSONResponse

# API imports
from app.api.v1 import router


app = FastAPI(
    title="Language Recognize",
    redoc_url="/redoc",
    description="Language recognition service.",
    version="0.0.1"
)

# Include router
app.include_router(router)


@app.get("/healthcheck")
def healthcheck() -> JSONResponse:
    """
    Basic health-check endpoint.
    """
    return JSONResponse({"status": "OK"}, status_code=200)
