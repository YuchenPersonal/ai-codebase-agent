from pathlib import Path

from .scanner import find_source_files
from .analyzer import analyze_source_files

def main():
    project_path = Path("D:/UE Projects/Xtreme")

    source_files = find_source_files(project_path)

    stats = analyze_source_files(source_files)

    print(f"Total source files: {stats.total_source_files}")
    print(f"Total USTRUCTs: {stats.total_ustructs}")
    print(f"Total UCLASSes: {stats.total_uclasses}")