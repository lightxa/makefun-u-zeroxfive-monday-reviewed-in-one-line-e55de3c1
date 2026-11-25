"""Monday, Reviewed in One Line.

Writes the funniest one-line review of my own Monday to
/output/entry.txt. One line, under 200 characters, nothing else.

Deterministic, standard library only, no network at runtime.
"""

from pathlib import Path

ENTRY = (
    "Monday: my inbox hit 47 unread before 9 a.m., the standup ran "
    "40 minutes, and my coffee went cold twice. One star."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
