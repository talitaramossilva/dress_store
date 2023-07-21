from pydantic import BaseModel


class ErrorSchema(BaseModel):
    """ Define the error message representation """
    message: str
