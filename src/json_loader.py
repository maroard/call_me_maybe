from pathlib import Path
from typing import Any
from json import JSONDecodeError, load


class JsonLoader:
    def __init__(self, path: Path) -> None:
        self.path = path

    def load(self) -> Any:
        try:
            with open(self.path, "r", encoding="utf-8") as file:
                return load(file)
        except JSONDecodeError as error:
            raise ValueError(
                f"Invalid JSON in {self.path}: {error.msg} "
                f"at line {error.lineno}, column {error.colno}"
            ) from error
        except OSError as error:
            raise OSError(
                f"Cannot read JSON file {self.path}: {error}") from error
