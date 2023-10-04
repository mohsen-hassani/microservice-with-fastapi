import dataclasses
from typing import NewType

UserID = NewType("UserID", int)
FeedbackID = NewType("FeedbackID", int)


@dataclasses.dataclass
class DBFeedback:
    id_: FeedbackID | None
    user_id: UserID | None
    feedback: str
