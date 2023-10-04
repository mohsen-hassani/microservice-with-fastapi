import uuid
from src.models.domains import DBFeedback, FeedbackID, UserID
from .base_database import BaseDatabase

USER_ID = UserID(265452349517802502818104800389817424405)
FEEDBACK1_ID = FeedbackID(3392721182899274928786147180529153895)
FEEDBACK2_ID = FeedbackID(165035723749407675732020667160399101349)
FEEDBACKS = {
    FEEDBACK1_ID: DBFeedback(id_=FEEDBACK1_ID, user_id=USER_ID, feedback="Great Feedback"),
    FEEDBACK2_ID: DBFeedback(id_=FEEDBACK2_ID, user_id=None, feedback="Bad Feedback")
}


class InMemoryDictDatabase(BaseDatabase):
    def __init__(self):
        self.__db: dict[int, DBFeedback] = FEEDBACKS

    def all(self) -> list[DBFeedback]:
        return list(self.__db.values())

    def insert(self, feedback: DBFeedback) -> FeedbackID:
        id_ = feedback.id_
        if id_ is None:
            id_ = self.get_new_id()
            feedback.id_ = FeedbackID(id_)
        self.__db[id_] = feedback
        return id_

    def get_new_id(self) -> int:
        id_ = uuid.uuid4().int
        while id_ in self.__db:
            id_ = uuid.uuid4().int
        return id_
