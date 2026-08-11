from __future__ import annotations

import typing

from biscuit.extensions import Extension

if typing.TYPE_CHECKING:
    from biscuit.api import ExtensionsAPI


class CodeRunner(Extension):
    """Run code snippets or files for multiple languages with one shortcut."""

    COMMAND_MAP = {
        "python": "python -u",
        "javascript": "node",
        "typescript": "ts-node",
        "c": "gcc $fileName -o $fileNameWithoutExt && ./$fileNameWithoutExt",
        "cpp": "g++ $fileName -o $fileNameWithoutExt && ./$fileNameWithoutExt",
        "rust": "cargo run",
        "go": "go run",
        "sh": "bash",
    }

    def __init__(self, api: ExtensionsAPI) -> None:
        super().__init__(api)
        self.api = api
        self.api.logger.info("Code Runner extension initialised.")

    def get_run_command(self, language: str, file_path: str) -> str | None:
        cmd_template = self.COMMAND_MAP.get(language.lower())
        if not cmd_template:
            return None
        return cmd_template.replace("$fileName", file_path)

    def install(self) -> None:
        self.api.logger.info("Code Runner extension installed.")
