from datetime import datetime, timedelta, timezone
from typing import List

from bson.objectid import ObjectId as BsonObjectId
from models.event import EventIn, EventOut
from service.private.event_query_functions import create_event, delete_event, find_event_by_id, update_event


class EventService:

    def find_one(self, event_id: str = None) -> EventOut:
        return find_event_by_id(event_id)

    def find_some(self) -> List[EventOut]:
        return [EventOut(id=BsonObjectId('64279d67325037253311cc50'), summary="test", event_start=datetime.now(timezone.utc), event_end=datetime.now(timezone.utc)+timedelta(minutes=30), all_day=True)]

    def create(self, event: EventIn = None) -> EventOut:
        return create_event(event=event)

    def update(self, event_id: str = None, event: EventIn = None) -> EventOut:
        return update_event(event_id=event_id, event=event)

    def delete(self, event_id: str = None) -> bool:
        return delete_event(event_id=event_id)