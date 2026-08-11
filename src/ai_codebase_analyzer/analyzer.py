from pathlib import Path

def analyze_source_files(file_paths: list[Path]):
    for file_path in file_paths:
        print(f"Analyzing: {file_path}")

        with file_path.open("r", encoding="utf-8") as file:
            contents = file.read()

            # Analyze contents here
            print(f" {len(contents)} characters")