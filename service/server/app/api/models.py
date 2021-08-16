from pydantic import BaseModel


class RecognizeRequest(BaseModel):
    """
    Request for the language recognition endpoint.
    """

    text: str  #: Text to classify
