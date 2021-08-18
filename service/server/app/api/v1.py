from fastapi import APIRouter
from fastapi.responses import JSONResponse

from ..exceptions import InputValidationErr
from ..core import handlers
from .models import RecognizeRequest

router = APIRouter(prefix="/api/v1")


@router.post("/identify-lang")
async def identify_lang(req: RecognizeRequest) -> JSONResponse:
    """
    Handler for the language recognition model.
    :param req: Request with a text to classify using the model.
    """
    try:
        text = req.text
        print("[TEXT]:", text)
        handler = handlers.LangRecModelHandler()
        out = handler.identify_lang(text)
        return JSONResponse(out, status_code=200)

    except InputValidationErr as e:
        out = {
            "error_message": str(e)
        }
        return JSONResponse(out, status_code=422)

    except Exception as e:
        out = {
            "error_message": str(e)
        }
        return JSONResponse(out, status_code=500)
