from fastapi import APIRouter, Body, Depends

from src.models.domains import UserID
from src.models.schemas import FeedbackSchema, FeedbackOutSchema
from src.dependencies import get_db, get_user_id
from src.services import NewFeedbackService, ListFeedbackService

feedback_public_router = APIRouter()


@feedback_public_router.get("/", response_model=list[FeedbackOutSchema])
def feedback_list(db=Depends(get_db)):
    service = ListFeedbackService(db=db)
    r = service.exec()
    return r


@feedback_public_router.post("/", response_model=FeedbackOutSchema)
def new_feedback(data: FeedbackSchema = Body(...), db=Depends(get_db), user_id: UserID | None = Depends(get_user_id)):
    service = NewFeedbackService(db=db)
    return service.exec(feedback=data, user_id=user_id)
