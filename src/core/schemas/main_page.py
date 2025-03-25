from pydantic import BaseModel


class MainBase(BaseModel):
    message: str = "Main_page"