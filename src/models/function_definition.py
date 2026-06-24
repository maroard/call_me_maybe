from __future__ import annotations

from pydantic import BaseModel, model_validator

from src.models.type_definition import TypeDefinition


class FunctionDefinition(BaseModel):
    name: str
    description: str
    parameters: dict[str, TypeDefinition]
    returns: TypeDefinition

    @model_validator(mode="after")
    def check_validity(self) -> FunctionDefinition:
        if not self.name.strip():
            raise ValueError(
                "Function name cannot be empty or contain only whitespaces"
            )

        if not self.description.strip():
            raise ValueError(
                f"Function '{self.name}' description cannot be empty "
                "or contain only whitespaces"
            )

        for parameter_name in self.parameters:
            if not parameter_name.strip():
                raise ValueError(
                    f"Function '{self.name}' has an empty parameter name"
                )

        return self
