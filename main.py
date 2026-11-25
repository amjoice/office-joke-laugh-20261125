"""Entry for make.fun bounty u-alfasurya91-make-the-ai-judge-laugh-6ed40225.

Program/v1 harness: writes one joke about office life to /output/entry.txt.
Gate: UTF-8 text of 1 to 200 characters, not only white space.
Deterministic, standard library only, no network.
"""

import os

ENTRY = "My boss's 'quick question' has a recurring invite, an agenda, and homework."


def write_entry() -> None:
    target = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    folder = os.path.dirname(target)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="\n") as out:
        out.write(ENTRY)


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
