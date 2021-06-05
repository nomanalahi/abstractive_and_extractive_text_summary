from pydantic import BaseModel

class Text(BaseModel):
    article: str