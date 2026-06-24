from typing import Any

from pydantic import ValidationError

from src.models.prompt_input import PromptInput
from src.models.function_definition import FunctionDefinition


class InputParser:
    def get_prompts(self, data: Any) -> list[PromptInput]:
        prompts: list[PromptInput] = []

        if not isinstance(data, list):
            raise ValueError("Prompts input must be a list")

        for index, element in enumerate(data):
            try:
                prompts.append(PromptInput.model_validate(element))
            except ValidationError as error:
                raise ValueError("Invalid prompt at index "
                                 f"{index}: {error}") from error

        return prompts

    def get_functions(self, data: Any) -> list[FunctionDefinition]:
        functions: list[FunctionDefinition] = []

        if not isinstance(data, list):
            raise ValueError("Functions definition input must be a list")

        for index, element in enumerate(data):
            try:
                functions.append(FunctionDefinition.model_validate(element))
            except ValidationError as error:
                raise ValueError("Invalid function definition at index "
                                 f"{index}: {error}") from error

        return functions
