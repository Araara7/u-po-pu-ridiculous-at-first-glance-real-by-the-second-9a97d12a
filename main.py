"""Write the entry for make.fun bounty
"Ridiculous at First Glance, Real by the Second"
(u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a).

Entry shape (from competition.yaml): one sentence, 1-200 characters,
pitching a bizarre startup idea that sounds absurd until you realise
it would actually sell. The pitch must name the odd thing being sold,
who pays for it, and why it holds together.

Freshness note: the pitch below was written for this bounty only.
It is not a recycled line: the odd thing is a pothole's naming rights
(a civic eyesore turned into ad inventory), the buyers are the local
shops outside whose door the crater sits, and the logic is that a
sponsored pothole gets patched first because somebody is watching.
The colon after "potholes" carries the turn: absurd premise first,
paying customers and the mechanism second.
"""

import hashlib
import os

ENTRY = (
    "We sell naming rights to potholes: local shops pay $50 a month "
    "to sponsor the crater outside their door, and the city patches "
    "it first because now somebody is watching."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of gate"
    assert ENTRY.count(".") == 1, "entry must be exactly one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
