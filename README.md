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
# File Read Assignment

This repository contains simple decorators to read and color text from files. The project provides an easy way to enhance file reading operations with custom styling and formatting capabilities.

## Features

- File reading decorators for enhanced text processing
- Custom text coloring and formatting
- Support for various file formats

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/file-read-assigment.git
cd file-read-assigment
```

2. Install dependencies using uv (recommended):
```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install the project in editable mode
uv pip install -e .
```

## Usage

Here's a simple example of how to use the file reading decorators:

```python
from file_read import read_file_decorator

@read_file_decorator
def process_file(file_path):
    # Your file processing logic here
    pass
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

