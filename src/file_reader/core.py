"""
A file reading library with support for:
- File reading using generators
- ANSI color text formatting via decorators
- Custom property getters/setters
- Static and class methods
- Operator overloading (__add__, __str__)
- Inheritance with extended functionality
"""
from typing import Generator, Union, List, Optional, Dict
from pathlib import Path
import os
import re


# ANSI Color Map for consistent color usage
ANSI_COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'end': '\033[0m'
}


def colorize(color: str = 'blue'):
    """
    A decorator that changes the color of text output using ANSI color codes.
    
    Args:
        color (str): Color name from ANSI_COLORS map
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, str):
                return f"{ANSI_COLORS.get(color, ANSI_COLORS['blue'])}{result}{ANSI_COLORS['end']}"
            return result
        return wrapper
    return decorator


def validate_file(func):
    """
    A decorator that validates if the file exists before executing the method.
    Skips validation for in-memory content created via from_string.
    """
    def wrapper(self, *args, **kwargs):
        if self._content is None and not self.filepath.exists():
            raise FileNotFoundError(f"File not found: {self.filepath}")
        return func(self, *args, **kwargs)
    return wrapper


class FileReader:
    """
    Base class for reading files using generators with various utilities.
    Provides core functionality for file reading and manipulation.
    """
    def __init__(self, filepath: Union[str, Path]):
        self._filepath = Path(filepath)
        self._content: Optional[str] = None

    @property
    def filepath(self) -> Path:
        """Get the file path."""
        return self._filepath

    @filepath.setter
    def filepath(self, value: Union[str, Path]) -> None:
        """Set the file path and reset cached content."""
        self._filepath = Path(value)
        self._content = None

    @property
    def filename(self) -> str:
        """Get the filename from the file path."""
        return self.filepath.name

    @property
    @validate_file
    def content(self) -> str:
        """Get the file content, loading it if necessary."""
        if self._content is None:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                self._content = f.read()
        return self._content

    @classmethod
    def from_string(cls, content: str, filepath: Union[str, Path]) -> 'FileReader':
        """Create a FileReader instance from a string."""
        instance = cls(filepath)
        instance._content = content
        return instance

    @staticmethod
    def is_text_file(filepath: Union[str, Path]) -> bool:
        """Check if a file is a text file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                f.read(1024)
            return True
        except (UnicodeDecodeError, FileNotFoundError):
            return False

    @validate_file
    def read_lines(self) -> Generator[str, None, None]:
        """Read the file line by line using a generator."""
        if self._content is not None:
            yield from self._content.splitlines()
        else:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                for line in f:
                    yield line.rstrip('\n')

    @validate_file
    def read_chunks(self, chunk_size: int = 1024) -> Generator[str, None, None]:
        """Read the file in chunks using a generator."""
        if self._content is not None:
            for i in range(0, len(self._content), chunk_size):
                yield self._content[i:i + chunk_size]
        else:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                while True:
                    chunk = f.read(chunk_size)
                    if not chunk:
                        break
                    yield chunk

    @property
    def lines(self) -> List[str]:
        """Get all lines as a list."""
        return list(self.read_lines())

    @property
    def word_count(self) -> int:
        """Count words in the file."""
        return len([word for word in self.content.split() if word])

    @colorize('blue')
    def __str__(self) -> str:
        """Return a string representation of the file content."""
        preview = self.content[:200] + ('...' if len(self.content) > 200 else '')
        return f"FileReader('{self.filepath}')\nContent:\n{preview}"

    def __add__(self, other: 'FileReader') -> 'FileReader':
        """Concatenate two files."""
        if not isinstance(other, FileReader):
            raise TypeError("Can only concatenate FileReader instances")
        
        new_content = f"{self.content.rstrip()}\n{other.content.lstrip()}"
        new_path = self.filepath.parent / f"{self.filepath.stem}_concat{self.filepath.suffix}"
        return self.from_string(new_content, str(new_path))


class ExtendedFileReader(FileReader):
    """
    Extended version of FileReader with additional text analysis features.
    """
    def __init__(self, filepath: Union[str, Path], case_sensitive: bool = True):
        super().__init__(filepath)
        self.case_sensitive = case_sensitive

    @property
    def word_frequencies(self) -> Dict[str, int]:
        """Count frequency of each word in the file."""
        words = self.content.split()
        if not self.case_sensitive:
            words = [word.lower() for word in words]
        
        frequencies = {}
        for word in words:
            if word: 
                frequencies[word] = frequencies.get(word, 0) + 1
        return frequencies

    def find_matches(self, pattern: str) -> List[str]:
        """Find all matches of a regex pattern in the file."""
        flags = 0 if self.case_sensitive else re.IGNORECASE
        return re.findall(pattern, self.content, flags=flags)

    def filter_lines(self, condition: str) -> List[str]:
        """Filter lines based on a condition string."""
        return [line for line in self.lines if eval(condition, {'line': line})]

    @staticmethod
    def merge_files(readers: List['FileReader']) -> 'ExtendedFileReader':
        """Merge multiple files into a single ExtendedFileReader."""
        if not readers:
            raise ValueError("No files to merge")
        
        combined_content = '\n'.join(reader.content.strip() for reader in readers)
        new_path = readers[0].filepath.parent / "merged.txt"
        return ExtendedFileReader.from_string(combined_content, str(new_path))

    @colorize('green')
    def __str__(self) -> str:
        """Return a fancy string representation."""
        return f"ExtendedFileReader('{self.filepath}')\nWords: {self.word_count}\nCase-sensitive: {self.case_sensitive}" 