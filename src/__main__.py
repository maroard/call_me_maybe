from argparse import ArgumentParser

from pydantic import ValidationError

from src.config import Config
from src.json_loader import JsonLoader
from src.input_parser import InputParser


def main() -> None:
    argument_parser = ArgumentParser()
    argument_parser.add_argument(
        "--functions_definition",
        default="data/input/functions_definition.json"
    )
    argument_parser.add_argument(
        "--input",
        default="data/input/function_calling_tests.json"
    )
    argument_parser.add_argument(
        "--output",
        default="data/output/function_calls.json"
    )

    args = argument_parser.parse_args()

    try:
        config = Config(
            functions_definition_path=args.functions_definition,
            input_path=args.input,
            output_path=args.output
        )

        raw_functions = JsonLoader(config.functions_definition_path).load()
        raw_prompts = JsonLoader(config.input_path).load()

        input_parser = InputParser()
        functions = input_parser.get_functions(raw_functions)
        prompts = input_parser.get_prompts(raw_prompts)

    except (ValidationError, ValueError, OSError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
