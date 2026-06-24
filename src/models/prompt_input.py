from __future__ import annotations

from pydantic import BaseModel, model_validator


class PromptInput(BaseModel):
    prompt: str

    @model_validator(mode="after")
    def check_validity(self) -> PromptInput:
        if not self.prompt.strip():
            raise ValueError("A prompt cannot be empty "
                             "or contain only whitespaces")
        return self
