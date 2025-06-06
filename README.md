``` ASCII
   ▄████████  ▄█   ▄█          ▄████████         ▄████████    ▄████████    ▄████████ ████████▄  
  ███    ███ ███  ███         ███    ███        ███    ███   ███    ███   ███    ███ ███   ▀███ 
  ███    █▀  ███▌ ███         ███    █▀         ███    ███   ███    █▀    ███    ███ ███    ███ 
 ▄███▄▄▄     ███▌ ███        ▄███▄▄▄           ▄███▄▄▄▄██▀  ▄███▄▄▄       ███    ███ ███    ███ 
▀▀███▀▀▀     ███▌ ███       ▀▀███▀▀▀          ▀▀███▀▀▀▀▀   ▀▀███▀▀▀     ▀███████████ ███    ███ 
  ███        ███  ███         ███    █▄       ▀███████████   ███    █▄    ███    ███ ███    ███ 
  ███        ███  ███▌    ▄   ███    ███        ███    ███   ███    ███   ███    ███ ███   ▄███ 
  ███        █▀   █████▄▄██   ██████████        ███    ███   ██████████   ███    █▀  ████████▀  
                  ▀                             ███    ███                                      
                         _              _                                 _   
                        /_\   ___  ___ (_)  __ _  _ __ ___    ___  _ __  | |_ 
                       //_\\ / __|/ __|| | / _` || '_ ` _ \  / _ \| '_ \ | __|
                      /  _  \\__ \\__ \| || (_| || | | | | ||  __/| | | || |_ 
                      \_/ \_/|___/|___/|_| \__, ||_| |_| |_| \___||_| |_| \__|
                                           |___/                              
```

# FileReader Library

## Features
- Generator-based file reading for memory efficiency
- File concatenation support
- Word frequency analysis
- Pattern matching with regex support
- Line filtering with custom predicates
- ANSI color text output
- Comprehensive test suite
- Type hints throughout the codebase


## Quick Start
```python
from file_reader import FileReader, ExtendedFileReader

# Basic usage
reader = FileReader("example.txt")
for line in reader.read_lines():
    print(line)

# Extended features
ext_reader = ExtendedFileReader("example.txt", case_sensitive=False)
frequencies = ext_reader.word_frequencies
matches = ext_reader.find_matches(r"\w+ing\b")  # Find words ending in 'ing'
filtered = ext_reader.filter_lines("len(line) > 50")  # Lines longer than 50 chars

# File concatenation
reader1 = FileReader("file1.txt")
reader2 = FileReader("file2.txt")
combined = reader1 + reader2
```

## Features in Detail
### FileReader Class
The base `FileReader` class provides essential file reading functionality:

- `read_lines()`: Generator for reading lines
- `read_chunks(chunk_size=1024)`: Generator for reading chunks
- `content`: Property for accessing full file content
- `lines`: Property for getting all lines as a list
- `word_count`: Property for counting words
- File concatenation via the `+` operator

### ExtendedFileReader Class
The `ExtendedFileReader` class extends `FileReader` with additional features:

- `word_frequencies`: Dictionary of word frequencies
- `find_matches(pattern)`: Find regex pattern matches
- `filter_lines(predicate)`: Filter lines using a predicate
- `merge_files(files)`: Merge multiple files
- Case-sensitive/insensitive text processing

### Decorators
- `@color_text(color)`: Add ANSI colors to text output
- `@validate_file`: Ensure file exists before operations

## Examples
See the `examples/usage.py` file for comprehensive examples of all features.

## Development
### Setup (pip)
```bash
git clone https://github.com/pixbs/file-read-assigment.git
cd file-reader

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate  # Windows

# Install dependencies
pip install -e ".[test]"
```
### Setup (uv)
```bash
git clone https://github.com/pixbs/file-read-assigment.git
cd file-read-assigment

# Create and activate a virtual environment using uv
uv venv
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate      # Windows

# Install dependencies
uv pip install -e ".[test]"
```

### Running Tests
```bash
pytest
```

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

