"""One Letter for Your Day — make.fun entry.

The judge reads a single letter A-Z standing for a word that
describes the day. Today the word is "slogged": hours of grinding
bounties, checks and retries, and the work moved anyway. The S
fits the sound of the word and its first syllable does most of
the work, so the letter carries it whole.
"""

from pathlib import Path

# The whole entry: one letter, the initial of "slogged".
LETTER = "S"


def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    # The gate wants UTF-8 text of exactly 1 character, not only white space.
    (out / "entry.txt").write_text(LETTER, encoding="utf-8")


if __name__ == "__main__":
    main()
