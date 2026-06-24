from pydantic import BaseModel

from src.models.type_definition import TypeDefinition


class FunctionCall(BaseModel):
    name: str
    parameters: dict[str, TypeDefinition]
