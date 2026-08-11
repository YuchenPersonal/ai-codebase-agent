from pathlib import Path

def find_source_files(project_path: Path) -> list[Path]:
    source_files = []

    if not project_path.exists():
        print("The project path does NOT exist")
        return source_files

    for item in project_path.rglob("*"):
        if (
            item.is_file() and 
            item.suffix in [".cpp", ".h"] and 
            "intermediate" not in str(item).lower()
        ):
            source_files.append(item)

    return source_files