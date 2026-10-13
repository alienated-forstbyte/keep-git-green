from pathlib import Path
import sys

COUNTER_FILE = Path(__file__).parent / "counter.txt"

def increment_counter(file_path: Path = COUNTER_FILE) -> int:
    """Read counter from file, increment by 1, and save it back."""
    current_value = 0
    if file_path.exists():
        try:
            content = file_path.read_text(encoding="utf-8").strip()
            if content:
                current_value = int(content)
        except ValueError:
            print(f"Warning: '{content}' is not a valid integer. Resetting to 0.", file=sys.stderr)
            current_value = 0

    new_value = current_value + 1
    file_path.write_text(f"{new_value}\n", encoding="utf-8")
    return new_value

if __name__ == "__main__":
    count = increment_counter()
    print(f"Counter incremented to: {count}")
