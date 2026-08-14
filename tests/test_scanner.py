from pathlib import Path
from ai_codebase_analyzer.scanner import find_source_files

def test_find_source_files_return_1_with_cpp_file(tmp_path):
    cpp_file = tmp_path / "test_source_file.cpp" # create a Path pointing to the file
    cpp_file.write_text("// test")               # actually create the file and write to it
    source_file_paths = find_source_files(tmp_path)
    assert len(source_file_paths) == 1

def test_find_source_files_return_1_with_heaher_file(tmp_path):
    cpp_file = tmp_path / "test_source_file..h"
    cpp_file.write_text("// test")
    source_file_paths = find_source_files(tmp_path)
    assert len(source_file_paths) == 1


def test_find_source_files_return_0_with_file_inside_intermediate(tmp_path):
    intermediate_dir = tmp_path / "intermediate"
    intermediate_dir.mkdir()

    cpp_file = intermediate_dir / "test_source_file.generated.cpp"
    cpp_file.write_text("// test")
    source_file_paths = find_source_files(tmp_path)
    assert len(source_file_paths) == 0