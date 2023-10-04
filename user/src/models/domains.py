import dataclasses
from typing import NewType

UserID = NewType("UserID", int)


@dataclasses.dataclass
class DBUser:
    id_: UserID | None
    email: str
    password: str
    first_name: str | None
    last_name: str | None
