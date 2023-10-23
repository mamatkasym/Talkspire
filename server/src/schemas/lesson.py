from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, Extra, HttpUrl, field_validator


class Level(StrEnum):
    BEGINNER = 'Beginner'
    INTERMEDIATE = 'Intermediate'
    ADVANCED = 'Advanced'


class Lesson(BaseModel):
    capacity: int = 10
    level: Level | None = None
    participants: list[int]
    start_time: datetime
    topic: str
    tutor: int
    zoom_link: str

    @field_validator('zoom_link')
    def validate_zoom_link(cls, link: HttpUrl):
        # TODO: implement it
        return link

    class Config:
        # ban properties that haven't been defined
        extra = Extra.forbid
