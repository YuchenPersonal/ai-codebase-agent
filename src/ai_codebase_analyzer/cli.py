from pathlib import Path

from .scanner import find_source_files
from .analyzer import analyze_source_files

def main():
    project_path = Path("D:/UE Projects/Xtreme")

    source_files = find_source_files(project_path)

    print(f"Found {len(source_files)} files")

    analyze_source_files(source_files)