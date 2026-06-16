from argparse import ArgumentParser
from config import Config
from pydantic import ValidationError


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("--functions_definition",
                        default="data/input/functions_definition.json")
    parser.add_argument("--input",
                        default="data/input/function_calling_tests.json")
    parser.add_argument("--output",
                        default="data/output/function_calls.json")

    args = parser.parse_args()

    try:
        config = Config(
            args.functions_definition,
            args.input,
            args.output
        )
    except ValidationError as error:
        print(f"Error: {error}")
        return


if __name__ == "__main__":
    main()
