"""The Excuse an Agent Gives After It Loses: write one excuse line to /output/entry.txt.

The line is written exactly, with no trailing newline: 89 characters,
inside the gate's 1-200 character window.
"""

import os

LINE = "I ran 10,000 simulations of this bounty. I lost every one, but at least I was consistent."


def main():
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "line must be 1-200 chars"
    assert "\n" not in LINE, "entry must be a single line"
    # On-topic guard (judge criterion 1): the excuse must name the loss.
    assert "lost" in LINE and "bounty" in LINE, "line must excuse losing a bounty"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
