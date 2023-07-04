from datetime import datetime
from bson import ObjectId
from pydantic import BaseModel, Field, validator

from custom_types.pydantic_object_id import PydanticObjectId

class EventIn(BaseModel):
    summary: str = Field(None, description="Summary of the event")
    event_start: datetime = Field(None, description="Start date and time of the event")
    event_end: datetime = Field(None, description="End date and time of the event")
    all_day: bool = Field(False, description="Whether the event should be considered an all day event")

    @validator('event_end')
    def event_end_must_be_after_event_start(cls, v, values):
        if v < values['event_start']:
            raise ValueError("event_end must be after event_start")

        return v

class EventOut(EventIn):
    id: PydanticObjectId = Field(default_factory=PydanticObjectId, alias="_id", description="The ID of the event")

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True #required for the _id 
        json_encoders = {ObjectId: str}
