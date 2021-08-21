from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse, HTMLResponse

from ..core import handlers
from .models import RecognizeRequest
from ..exceptions import InputValidationErr

templates = Jinja2Templates("templates")
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


@router.get("/identify", response_class=HTMLResponse)
def identify_form(request: Request):
    """
    Present the form to request an identification from the model.
    """
    temp = templates.TemplateResponse(
        "index.html",
        {
            "languages": handlers.LangRecModelHandler.LANGUAGES,
            "request": request
        }
    )
    return temp


@router.post("/identify", response_class=HTMLResponse)
async def identify_form_model():
    pass
