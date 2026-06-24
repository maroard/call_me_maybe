from __future__ import annotations
from pathlib import Path

from pydantic import BaseModel, model_validator


class Config(BaseModel):
    functions_definition_path: Path
    input_path: Path
    output_path: Path

    @model_validator(mode="after")
    def check_validity(self) -> Config:
        not_existing_paths: list[Path] = []
        not_file_paths: list[Path] = []
        for element in [self.functions_definition_path, self.input_path]:
            if not element.exists():
                not_existing_paths.append(element)
            if element.exists() and not element.is_file():
                not_file_paths.append(element)

        if not_existing_paths:
            not_existing_paths_label = ", ".join(
                str(path) for path in not_existing_paths)
            not_existing_paths_error_label: str = "does not exist"
            if len(not_existing_paths) > 1:
                not_existing_paths_error_label = "do not exist"
            raise ValueError(
                f"{not_existing_paths_label} "
                f"{not_existing_paths_error_label}")

        if not_file_paths:
            not_file_paths_label = ", ".join(
                str(path) for path in not_file_paths)
            not_file_paths_error_label: str = "is not a file"
            if len(not_file_paths) > 1:
                not_file_paths_error_label = "are not files"
            raise ValueError(
                f"{not_file_paths_label} "
                f"{not_file_paths_error_label}")

        not_json_files: list[Path] = []
        for path in [
            self.functions_definition_path, self.input_path, self.output_path
        ]:
            if path.suffix != ".json":
                not_json_files.append(path)

        if not_json_files:
            not_json_files_label = ", ".join(
                str(file) for file in not_json_files)
            not_json_files_error_label: str = "is not a json file"
            if len(not_json_files) > 1:
                not_json_files_error_label = "are not json files"
            raise ValueError(
                f"{not_json_files_label} "
                f"{not_json_files_error_label}")

        return self
