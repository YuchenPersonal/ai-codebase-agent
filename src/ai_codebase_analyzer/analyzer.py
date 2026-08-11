import re
from dataclasses import dataclass
from pathlib import Path

@dataclass
class AnalysisStats:
    total_source_files: int = 0
    total_ustructs: int = 0
    total_uclasses: int = 0

def analyze_source_files(file_paths: list[Path]) -> AnalysisStats:

    stats = AnalysisStats()

    for file_path in file_paths:
        stats.total_source_files += 1

        with file_path.open("r", encoding="utf-8") as file:
            contents = file.read()

            ustruct_pattern = r'USTRUCT\s*\([^)]*\)\s*struct\s+(?:\w+\s+)*(\w+)'
            ustructs = re.findall(ustruct_pattern, contents)
            for ustruct in ustructs:
                stats.total_ustructs += 1

            uclass_pattern = r'UCLASS\s*\([^)]*\)\s*class\s+(?:\w+\s+)*(\w+)'
            uclasses = re.findall(uclass_pattern, contents)
            for uclass in uclasses:
                stats.total_uclasses += 1

    return stats