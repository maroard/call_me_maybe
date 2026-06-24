from pydantic import BaseModel

from src.models.prompt_input import PromptInput
from src.models.type_definition import TypeDefinition


class FunctionCallOutput(BaseModel):
    prompt: PromptInput
    name: str
    parameters: dict[str, TypeDefinition]
