"""The One-Line Exit — writes one funny one-line resignation letter.

Entrypoint for the make.fun bounty "The One-Line Exit"
(u-kreutzx-the-one-line-exit-1dc652d1). Deterministic, no network,
no environment, no file reads: it writes a single fixed line to
/output/entry.txt, with no trailing newline.
"""

import os

ENTRY = (
    "I resign effective immediately — the office plant has been "
    "promoted above me twice now, and honestly, it earned it."
)


def main() -> None:
    # Gate: UTF-8 text of 1-140 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 140, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    # Verify the write round-trips byte for byte: what the judge
    # reads must be exactly ENTRY, nothing more, nothing less.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == ENTRY.encode("utf-8"), "written bytes differ from ENTRY"
    assert not written.endswith(b"\n"), "no trailing newline allowed"


if __name__ == "__main__":
    main()
