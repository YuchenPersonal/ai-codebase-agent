from pathlib import Path

def find_source_files(project_path: Path) -> list[Path]:
    source_files = []

    if not project_path.exists():
        print("The project path does NOT exist")
        return source_files

    for path in project_path.rglob("*"):
        if (
            path.is_file() and 
            path.suffix in [".cpp", ".h"] and 
            "intermediate" not in str(path).lower()
        ):
            source_files.append(path)

    return source_files