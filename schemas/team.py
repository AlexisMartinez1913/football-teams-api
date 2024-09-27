from pydantic import BaseModel, Field
from typing import Optional


class Team(BaseModel):
    id: Optional[int] = None
    name: str = Field(min_length=5, max_length=100)
    founded: int
    country: str = Field(min_length=5, max_length=200)
    stadium: str
    coach: str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Liverpool FC",
                "founded": 1892,
                "country": "England",
                "stadium": "Anfield",
                "coach": "Arne Slot"
            }
        }
