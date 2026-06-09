# 📘 Assignment: Python Text Processing

## 🎯 Objective

Master string manipulation and file I/O in Python by building utilities to process, parse, and transform text data.

## 📝 Tasks

### 🛠️ Build a Text Processing Toolkit

#### Description
Create a Python script that reads text from files, processes it using string methods and regular expressions, and outputs the results. The script should handle multiple text processing operations like counting word frequencies, finding patterns, replacing text, and formatting output.

#### Requirements
Completed program should:

- Read text from a file or accept user input.
- Perform case-insensitive word frequency counting and display top N words.
- Use regular expressions to find and extract patterns (e.g., email addresses, URLs, phone numbers).
- Implement text statistics: character count, word count, sentence count, average word length.
- Search and replace text based on user-defined patterns.
- Handle file I/O errors gracefully with meaningful error messages.
- Write processed results to an output file.
- Support at least 2-3 different text processing modes (e.g., frequency analysis, pattern extraction, text statistics).

Example usage:

```bash
python starter-code.py input.txt --mode frequency --top 10
python starter-code.py input.txt --mode stats
python starter-code.py input.txt --mode extract --pattern "email"
```

Starter code: see `starter-code.py` in this folder.
