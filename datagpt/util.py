from pathlib import Path


def get_project_root():
    current_path = Path.cwd()
    while True:
        if (current_path / ".project_root").exists():
            return current_path
        parent_path = current_path.parent
        if parent_path == current_path:
            raise Exception("Project root not found.")
        current_path = parent_path


root = get_project_root()
