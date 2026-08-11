import argparse
from pathlib import Path

from .scanner import find_source_files
from .analyzer import analyze_source_files

def main():

    parser = argparse.ArgumentParser(
        description="Analyze a Unreal Engine C++ codebase"
    )

    parser.add_argument(
        "project_path",
        type=Path,
        help="Path to the project to analyze"
    )

    args = parser.parse_args()

    project_path = args.project_path

    source_files = find_source_files(project_path)

    stats = analyze_source_files(source_files)

    print(f"Total source files: {stats.total_source_files}")
    print(f"Total USTRUCTs: {stats.total_ustructs}")
    print(f"Total UCLASSes: {stats.total_uclasses}")