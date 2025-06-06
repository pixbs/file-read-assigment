"""
Extended FileReader with additional functionality.
"""
from typing import Dict, List, Optional, Pattern
import re
from pathlib import Path
from .core import FileReader, color_text


class ExtendedFileReader(FileReader):
    """
    Extended FileReader class with additional text analysis features.
    """
    def __init__(self, filepath: Path, case_sensitive: bool = True):
        super().__init__(filepath)
        self.case_sensitive = case_sensitive
        self._word_frequencies: Optional[Dict[str, int]] = None

    @property
    def word_frequencies(self) -> Dict[str, int]:
        """Get word frequencies in the file."""
        if self._word_frequencies is None:
            words = self.content.split()
            if not self.case_sensitive:
                words = [word.lower() for word in words]
            self._word_frequencies = {
                word: words.count(word) for word in set(words)
            }
        return self._word_frequencies

    @color_text('green')
    def find_matches(self, pattern: str) -> List[str]:
        """Find all matches of a regex pattern in the file."""
        flags = 0 if self.case_sensitive else re.IGNORECASE
        compiled_pattern: Pattern = re.compile(pattern, flags)
        return [match.group() for match in compiled_pattern.finditer(self.content)]

    def filter_lines(self, predicate: str) -> List[str]:
        """Filter lines based on a predicate string."""
        return [
            line for line in self.read_lines()
            if eval(predicate, {"line": line})
        ]

    @staticmethod
    def merge_files(files: List['ExtendedFileReader']) -> 'ExtendedFileReader':
        """Merge multiple files into a new one."""
        if not files:
            raise ValueError("No files provided for merging")
        
        merged_content = '\n'.join(f.content for f in files)
        new_path = files[0].filepath.parent / "merged_file.txt"
        return ExtendedFileReader.from_string(merged_content, new_path)

    def __str__(self) -> str:
        """Enhanced string representation with word count."""
        base_str = super().__str__()
        return f"{base_str}\nWord count: {self.word_count}" 