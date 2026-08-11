from pathlib import Path
import re

def analyze_source_files(file_paths: list[Path]):
    for file_path in file_paths:
        print(f"Analyzing: {file_path}")

        with file_path.open("r", encoding="utf-8") as file:
            contents = file.read()

            ustruct_pattern = r'USTRUCT\s*\([^)]*\)\s*struct\s+(?:\w+\s+)*(\w+)'
            ustructs = re.findall(ustruct_pattern, contents)
            for ustruct in ustructs:
                print(ustruct)
            
            uclass_pattern = r'UCLASS\s*\([^)]*\)\s*class\s+(?:\w+\s+)*(\w+)'
            uclasses = re.findall(uclass_pattern, contents)
            for uclass in uclasses:
                print(uclass)