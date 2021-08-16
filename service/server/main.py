from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Language Recognize",
    redoc_url="/redoc",
    description="Language recognition service."
)


@app.get("/healthcheck")
def healthcheck() -> JSONResponse:
    """
    Basic health-check endpoint.
    """
    return JSONResponse({"status": "OK"}, status_code=200)
