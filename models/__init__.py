from pydantic import BaseModel

class Event(BaseModel):
    id: int
    name = 'Jane Doe'