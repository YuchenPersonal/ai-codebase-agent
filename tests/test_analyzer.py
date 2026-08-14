from pathlib import Path
from ai_codebase_analyzer.analyzer import analyze_source_files

def test_analyze_source_files_find_1_uclass(tmp_path):
    source_file = tmp_path / "test.h"
    source_file.write_text("UCLASS() class UMyTestClass{};")

    file_paths = [source_file]

    stats = analyze_source_files(file_paths)

    assert stats.total_uclasses == 1

def test_analyze_source_files_find_1_ustruct(tmp_path):
    source_file = tmp_path / "test.h"
    source_file.write_text("USTRUCT() struct FMyTestStruct{};")

    file_paths = [source_file]

    stats = analyze_source_files(file_paths)

    assert stats.total_ustructs == 1

def test_analyze_source_files_find_2_source_files(tmp_path):
    source_file = tmp_path / "test.h"
    source_file.write_text("UCLASS() class UMyTestClass{};")

    source_file2 = tmp_path / "test.cpp"
    source_file2.write_text("test")

    file_paths = [source_file, source_file2]

    stats = analyze_source_files(file_paths)

    assert stats.total_source_files == 2