from sqlmodel import SQLModel, Field


# table=True convierte este modelo en la tabla student.
class Student(SQLModel, table=True):

    id: int | None = Field(
        default=None,
        primary_key=True
    )

    name: str

    email: str

    semester: int

    active: bool = True
