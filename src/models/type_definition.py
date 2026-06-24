from __future__ import annotations
from typing import Literal

from pydantic import BaseModel


type TypeValue = Literal["string", "number", "boolean"]


class TypeDefinition(BaseModel):
    type: TypeValue
