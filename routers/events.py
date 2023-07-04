from typing import Annotated, List
from fastapi import APIRouter, Body, HTTPException, Path, Response, status
from models.event import EventIn, EventOut

from service.event_service import EventService

router = APIRouter(
    prefix="/api/events",
    tags=["events"],
    responses={404: {"description": "Not found"}, 204: {"description": "No Content"}},
)

@router.post("/", summary="Create an event")
async def create(
    event: Annotated[EventIn, Body(description="The event with params to be updated")]
    ) -> EventOut:
    """
    Create a new event with the values in event
    """

    return event_service().create(event=event)

@router.get("/", summary="List events")
async def list() -> List[EventOut]:
    """
    List the events that match the specified query parameters
    """

    return event_service().find_some()

@router.put("/{event_id}", summary="Update an event")
async def update(
    event_id: Annotated[str, Path(description="The ID of the event to update")],
    event: Annotated[EventIn, Body(description="The event with params to be updated")]
    ) -> EventOut:
    """
    Updates the event specified by event_id with the values in event
    """

    return  event_service().update(event_id=event_id, event=event)

@router.get("/{event_id}", summary="Show an event")
async def show(
    event_id: Annotated[str, Path(description="The ID of the event to get")]
    ) -> EventOut:
    """
    Returns the event specified by event_id
    """
    return  event_service().find_one(event_id)

@router.delete("/{event_id}", summary="Delete an event")
async def delete(
    event_id: Annotated[str, Path(description="The ID of the event to delete")]
    ) -> Response:
    """
    Deletes the event specified by event_id
    """

    if event_service().delete(event_id=event_id):
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Event with ID {event_id} not found")

def event_service():
    return EventService()