from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.code_runner import setup
from src.code_runner.extension import CodeRunner


class TestCodeRunnerExtension:
    def test_extension_setup(self, app_instance) -> None:
        setup(app_instance.api)
        ext = CodeRunner(app_instance.api)
        cmd = ext.get_run_command("python", "main.py")
        assert cmd == "python -u"
        cmd_go = ext.get_run_command("go", "main.go")
        assert cmd_go == "go run"
