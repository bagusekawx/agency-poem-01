"""agency-poem-01 entry: write one poem about agency to /output/entry.txt.

Standard library only. Deterministic: the same bytes on every run.
"""

# v1: 962 chars, 29 lines; two local runs byte-identical.

import os
from pathlib import Path

POEM = """Four Hands

My father played the piano every night
after supper, the same six pieces,
while my mother washed the dishes
and the water ran, and ran.

He played them from memory, and the memory
went first. The hands went next.
Now he sits beside the piano
and listens to the bench creak when I sit down.

I gave the agent his recordings,
fifty years of Sundays. It had him
by Tuesday. It plays the pieces now
through the speaker on the piano,
every note right, every pause in place,
the pedal exactly where he put it.

It plays them better than he did.
Some nights I turn it off.

On Sundays I sit down myself.
My hands are stiff. I learned late.
I play the first piece, the slow one,
and I miss the turn in the middle,
the same three notes, every time.

He puts his hand on my shoulder
when I get them wrong.
He never did that when they were right.

The pieces are its now.
It can have them, all six, perfect.
The wrong notes are mine.
That is where he still is.
"""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
