import dataclasses

from src.databases import BaseDatabase
from src.models.schemas import FeedbackSchema, FeedbackOutSchema
from src.models.domains import DBFeedback, UserID


class BaseService:
    def __init__(self, db: BaseDatabase):
        self.db = db


class ListFeedbackService(BaseService):
    def exec(self) -> list[FeedbackOutSchema]:
        feedbacks: list[DBFeedback] = self.db.all()
        return [FeedbackOutSchema(**dataclasses.asdict(feedback)) for feedback in feedbacks]


class NewFeedbackService(BaseService):
    def exec(self, feedback: FeedbackSchema, user_id: UserID | None) -> FeedbackOutSchema:
        db_feedback = DBFeedback(**feedback.model_dump(), user_id=user_id, id_=None)
        self.db.insert(db_feedback)
        return FeedbackOutSchema(**dataclasses.asdict(db_feedback))

