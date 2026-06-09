import re
import sys
from collections import Counter
from pathlib import Path


def load_text(file_path):
    """Load text from a file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)


def word_frequency(text, top_n=10):
    """Count word frequencies and return top N words."""
    words = re.findall(r"\b[a-z]+\b", text.lower())
    counter = Counter(words)
    return counter.most_common(top_n)


def text_statistics(text):
    """Calculate text statistics."""
    char_count = len(text)
    word_count = len(re.findall(r"\b\w+\b", text))
    sentence_count = len(re.split(r"[.!?]+", text)) - 1
    avg_word_len = char_count / word_count if word_count > 0 else 0

    return {
        "characters": char_count,
        "words": word_count,
        "sentences": sentence_count,
        "avg_word_length": round(avg_word_len, 2),
    }


def extract_patterns(text, pattern_type="email"):
    """Extract specific patterns from text."""
    patterns = {
        "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "url": r"https?://[^\s]+",
        "phone": r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b",
    }

    pattern = patterns.get(pattern_type)
    if not pattern:
        return []

    return re.findall(pattern, text)


def main():
    if len(sys.argv) < 2:
        print("Usage: python starter-code.py <file_path> [--mode MODE] [--top N]")
        print("Modes: frequency, stats, extract")
        sys.exit(1)

    file_path = sys.argv[1]
    mode = "frequency"
    top_n = 10

    for i, arg in enumerate(sys.argv[2:], 2):
        if arg == "--mode" and i + 1 < len(sys.argv):
            mode = sys.argv[i + 1]
        elif arg == "--top" and i + 1 < len(sys.argv):
            top_n = int(sys.argv[i + 1])

    text = load_text(file_path)

    if mode == "frequency":
        print(f"Top {top_n} most common words:")
        for word, count in word_frequency(text, top_n):
            print(f"  {word}: {count}")

    elif mode == "stats":
        stats = text_statistics(text)
        print("Text Statistics:")
        for key, value in stats.items():
            print(f"  {key}: {value}")

    elif mode == "extract":
        pattern_type = "email"
        for arg in sys.argv:
            if arg == "--pattern" and sys.argv.index(arg) + 1 < len(sys.argv):
                pattern_type = sys.argv[sys.argv.index(arg) + 1]

        results = extract_patterns(text, pattern_type)
        print(f"Found {len(results)} {pattern_type} addresses:")
        for result in results[:10]:
            print(f"  {result}")

    else:
        print(f"Unknown mode: {mode}")


if __name__ == "__main__":
    main()
