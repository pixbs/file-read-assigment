"""
Unit tests for the FileReader library.
"""
import pytest
from pathlib import Path
import re
from file_reader import FileReader, ExtendedFileReader


@pytest.fixture
def sample_file(tmp_path):
    """Create a sample file for testing."""
    file_path = tmp_path / "test.txt"
    content = (
        "Hello World\n"
        "This is a test file\n"
        "With multiple lines\n"
        "Hello again\n"
        "Testing Testing 123"
    )
    file_path.write_text(content)
    return file_path


@pytest.fixture
def another_file(tmp_path):
    """Create another sample file for testing."""
    file_path = tmp_path / "another.txt"
    content = "Another file\nFor testing concatenation"
    file_path.write_text(content)
    return file_path


class TestFileReader:
    """Test suite for the base FileReader class."""

    def test_initialization(self, sample_file):
        """Test FileReader initialization."""
        reader = FileReader(sample_file)
        assert reader.filepath == sample_file
        assert reader.filename == "test.txt"
        assert reader._content is None

    def test_content_property(self, sample_file):
        """Test content property and caching."""
        reader = FileReader(sample_file)
        content = reader.content
        assert "Hello World" in content
        assert reader._content is not None
        
        reader.filepath = "new_path.txt"
        assert reader._content is None

    def test_file_reading_methods(self, sample_file):
        """Test various file reading methods."""
        reader = FileReader(sample_file)
        
        lines = list(reader.read_lines())
        assert len(lines) == 5
        assert lines[0] == "Hello World"
        
        chunks = list(reader.read_chunks(chunk_size=20))
        assert len(chunks) > 0
        assert isinstance(chunks[0], str)

        assert len(reader.lines) == 5
        assert reader.lines[0] == "Hello World"

    def test_word_count(self, sample_file):
        """Test word counting functionality."""
        reader = FileReader(sample_file)
        assert reader.word_count == 15

    def test_file_concatenation(self, sample_file, another_file):
        """Test file concatenation using __add__."""
        reader1 = FileReader(sample_file)
        reader2 = FileReader(another_file)
        combined = reader1 + reader2
        
        assert isinstance(combined, FileReader)
        assert combined.word_count == 20
        assert "test_concat.txt" in str(combined.filepath)

    def test_from_string(self):
        """Test creating FileReader from string."""
        content = "Test content"
        reader = FileReader.from_string(content, "test.txt")
        assert reader.content == content
        assert reader.filepath.name == "test.txt"

    def test_is_text_file(self, sample_file):
        """Test text file detection."""
        assert FileReader.is_text_file(sample_file) is True

    def test_file_not_found(self):
        """Test handling of non-existent files."""
        reader = FileReader("nonexistent.txt")
        with pytest.raises(FileNotFoundError):
            _ = reader.content

    def test_string_representation(self, sample_file):
        """Test string representation."""
        reader = FileReader(sample_file)
        str_repr = str(reader)
        assert "FileReader" in str_repr
        assert "Content:" in str_repr


class TestExtendedFileReader:
    """Test suite for the ExtendedFileReader class."""

    def test_initialization(self, sample_file):
        """Test ExtendedFileReader initialization."""
        reader = ExtendedFileReader(sample_file, case_sensitive=False)
        assert isinstance(reader, FileReader)
        assert reader.case_sensitive is False

    def test_word_frequencies(self, sample_file):
        """Test word frequency counting."""
        reader = ExtendedFileReader(sample_file)
        frequencies = reader.word_frequencies
        assert frequencies["Hello"] == 2
        assert frequencies["Testing"] == 2

        reader_ci = ExtendedFileReader(sample_file, case_sensitive=False)
        frequencies_ci = reader_ci.word_frequencies
        assert frequencies_ci["hello"] == 2
        assert frequencies_ci["testing"] == 2

    def test_find_matches(self, sample_file):
        """Test pattern matching."""
        reader = ExtendedFileReader(sample_file)
        
        matches = reader.find_matches(r"Hello \w+")
        assert len(matches) == 2
        assert matches[0] == "Hello World"
        assert matches[1] == "Hello again"
        
        reader.case_sensitive = False
        matches = reader.find_matches(r"hello \w+")
        assert len(matches) == 2

    def test_filter_lines(self, sample_file):
        """Test line filtering."""
        reader = ExtendedFileReader(sample_file)
        
        hello_lines = reader.filter_lines("'Hello' in line")
        assert len(hello_lines) == 2
        
        test_lines = reader.filter_lines("'test' in line.lower() and len(line) > 10")
        assert len(test_lines) == 2

    def test_merge_files(self, sample_file, another_file):
        """Test file merging."""
        reader1 = ExtendedFileReader(sample_file)
        reader2 = ExtendedFileReader(another_file)
        
        merged = ExtendedFileReader.merge_files([reader1, reader2])
        assert isinstance(merged, ExtendedFileReader)
        assert merged.word_count == 20
        
        with pytest.raises(ValueError):
            ExtendedFileReader.merge_files([])

    def test_string_representation(self, sample_file):
        """Test extended string representation."""
        reader = ExtendedFileReader(sample_file)
        str_repr = str(reader)
        assert "ExtendedFileReader" in str_repr
        assert "Words:" in str_repr
        assert "Case-sensitive:" in str_repr 