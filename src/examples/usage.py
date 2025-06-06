"""
Example usage of the FileReader library demonstrating core and extended features.
"""
from pathlib import Path
from file_reader import FileReader, ExtendedFileReader


def create_sample_files(base_path: Path):
    """Create sample files for demonstration."""
    
    sample_path = base_path / "sample.txt"
    sample_path.write_text(
        "Hello World!\n"
        "This is a sample file.\n"
        "It has multiple lines.\n"
        "Hello again!\n"
        "Testing, testing, 1-2-3."
    )

    another_path = base_path / "another.txt"
    another_path.write_text(
        "This is another file.\n"
        "It will be concatenated.\n"
        "More testing content here."
    )

    return sample_path, another_path


def demonstrate_basic_features(sample_path: Path):
    """Demonstrate basic FileReader features."""
    print("\n=== Basic FileReader Demo ===")
    reader = FileReader(sample_path)
    
    print("\nReading file line by line:")
    for line in reader.read_lines():
        print(f"  {line}")

    print("\nReading in chunks:")
    for chunk in reader.read_chunks(chunk_size=20):
        print(f"  Chunk: {chunk!r}")

    print("\nFile properties:")
    print(f"  Word count: {reader.word_count}")
    print(f"  Line count: {len(reader.lines)}")
    print(f"  Filename: {reader.filename}")

    print("\nString representation:")
    print(reader)


def demonstrate_extended_features(sample_path: Path):
    """Demonstrate ExtendedFileReader features."""
    print("\n=== Extended FileReader Demo ===")
    ext_reader = ExtendedFileReader(sample_path, case_sensitive=False)
    
    print("\nWord frequencies:")
    for word, count in sorted(ext_reader.word_frequencies.items()):
        print(f"  {word}: {count}")

    print("\nFinding patterns:")
    matches = ext_reader.find_matches(r"\w+ing\b")
    print(f"Words ending in 'ing': {matches}")

    print("\nFiltering lines:")
    has_hello = ext_reader.filter_lines("'hello' in line.lower()")
    print("Lines containing 'hello':")
    for line in has_hello:
        print(f"  {line}")

    print("\nString representation:")
    print(ext_reader)


def demonstrate_file_operations(sample_path: Path, another_path: Path):
    """Demonstrate file operations like concatenation and merging."""
    print("\n=== File Operations Demo ===")
    
    reader1 = FileReader(sample_path)
    reader2 = FileReader(another_path)
    combined = reader1 + reader2
    print("\nConcatenated files:")
    print(combined)

    readers = [reader1, reader2]
    merged = ExtendedFileReader.merge_files(readers)
    print("\nMerged files:")
    print(merged)
    print(f"Total words in merged file: {merged.word_count}")


def cleanup_files(sample_path: Path, another_path: Path):
    """Clean up sample files."""
    for path in [sample_path, another_path]:
        if path.exists():
            path.unlink()


def main():
    """Main demonstration function."""
    base_path = Path.cwd()
    sample_path, another_path = create_sample_files(base_path)

    try:
        demonstrate_basic_features(sample_path)
        demonstrate_extended_features(sample_path)
        demonstrate_file_operations(sample_path, another_path)
    finally:
        cleanup_files(sample_path, another_path)


if __name__ == "__main__":
    main()

