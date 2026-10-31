from pydantic import BaseModel, Field


# Esquema de entrada para crear estudiantes.
class StudentCreate(BaseModel):
    name: str = Field(min_length=3, max_length=80)
    # El correo es obligatorio y no puede ser vacío.
    email: str = Field(min_length=1)
    semester: int = Field(ge=1, le=10)
    active: bool = True


# Esquema de salida.
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    semester: int
    active: bool
