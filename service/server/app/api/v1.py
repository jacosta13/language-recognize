from fastapi import APIRouter
from fastapi.responses import JSONResponse

from .models import RecognizeRequest

router = APIRouter(prefix="/api/v1")


@router.post("/identify-lang")
def identify_lang(req: RecognizeRequest) -> JSONResponse:
    """
    Handler for the language recognition model.
    :param req: Request with a text to classify using the model.
    """
    text = req.text
    print("[TEXT]:", text)
    out = {
        "language": "Gibberish",
        "confidence": 0.99
    }
    return JSONResponse(out, status_code=200)
