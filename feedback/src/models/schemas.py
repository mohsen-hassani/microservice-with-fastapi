from pydantic import BaseModel

from src.models.domains import FeedbackID, UserID


class FeedbackSchema(BaseModel):
    feedback: str


class FeedbackOutSchema(BaseModel):
    id_: FeedbackID
    user_id: UserID | None
    feedback: str
