import dataclasses


@dataclasses.dataclass
class DBUser:
    id_: int | None
    email: str
    password: str
    first_name: str | None
    last_name: str | None
