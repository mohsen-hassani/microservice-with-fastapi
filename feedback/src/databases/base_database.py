from abc import ABC, abstractmethod
from models.domains import DBFeedback, FeedbackID


class BaseDatabase(ABC):
    @abstractmethod
    def all(self) -> list[DBFeedback]:
        raise NotImplementedError()

    @abstractmethod
    def insert(self, data: DBFeedback) -> FeedbackID:
        raise NotImplementedError()
