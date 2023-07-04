from bson import ObjectId
from fastapi import HTTPException, status
from db import mongo_collection

from models.event import EventIn, EventOut

def find_event_by_id(event_id: str = None):
    with mongo_collection('events') as events:
        if (event := events.find_one({"_id": ObjectId(event_id)})) is not None:
            return EventOut(**event)

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Event with ID {event_id} not found")
    
def create_event(event: EventIn = None):
    with mongo_collection('events') as events:
        new_event_id = events.insert_one(event.dict()).inserted_id 
        return EventOut(**events.find_one({"_id": new_event_id}))

def update_event(event_id: str = None,event: EventIn = None):
    event_updates = {k: v for k, v in event.dict().items() if v is not None}

    with mongo_collection('events') as events:
        update_result = events.update_one( {"_id": ObjectId(event_id)}, {"$set": event_updates})

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Event with ID {event_id} not found")

        if (event := events.find_one({"_id": ObjectId(event_id)})) is not None:
            return EventOut(**event)
        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Event with ID {event_id} not found")

def delete_event(event_id: str = None):
    with mongo_collection('events') as events:
        delete_result = events.delete_one({"_id": ObjectId(event_id)})

        return True if (delete_result.deleted_count == 1) else False
