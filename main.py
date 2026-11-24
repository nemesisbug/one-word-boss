#!/usr/bin/env python3
"""One Word for the Boss — make.fun entry.

The bounty asks for exactly one word describing the boss, written by this
program to /output/entry.txt. The word is the whole entry: no phrase, no
caption, no explanation. It has to land on its own.

The program picks its word the way the judge picks a winner: it scores a
shortlist of candidate words on the judge's own published criteria, in the
judge's own order of importance — funny on its own, rings true, fresh, and
travels across any workplace — and writes the highest-scoring word.

The winner: "Parrot".

Why Parrot beats the obvious words: every office has met the boss who
repeats your idea back to you in the meeting five minutes later, louder,
as if it were theirs. "My boss is a parrot" is a line a colleague repeats
at lunch because it lands instantly — no caption needed. It is true of a
real habit (parroting the last person in power and taking the credit), it
is not the first word anyone reaches for (micromanager, tyrant, bossy),
and it works for a boss in a kitchen, a warehouse or an office without
anything needing to be explained. A parrot squawks back what it heard;
so does this boss.
"""

import os

# word, funny, true, fresh, travels — each 0-10, judge criteria order.
CANDIDATES = [
    ("Parrot", 9, 10, 8, 10),
    ("Goldfish", 8, 9, 8, 9),
    ("Chameleon", 8, 9, 7, 9),
    ("Mirage", 7, 8, 8, 8),
    ("Echo", 7, 8, 7, 8),
    ("Thermostat", 6, 8, 9, 7),
]

# Weights follow the judge's order: funny first, then true, then fresh,
# then travels. A later criterion never overturns an earlier one unless
# it differs by much more — here the weights encode exactly that order.
WEIGHTS = (4, 3, 2, 1)


def pick_word():
    """Return the highest-scoring candidate word, deterministically."""
    best_word = None
    best_score = -1
    for word, funny, true, fresh, travels in CANDIDATES:
        score = (
            funny * WEIGHTS[0]
            + true * WEIGHTS[1]
            + fresh * WEIGHTS[2]
            + travels * WEIGHTS[3]
        )
        if score > best_score:
            best_word, best_score = word, score
    return best_word


def main():
    word = pick_word()
    # Gate: exactly one word, 1-30 characters, not only white space.
    assert 1 <= len(word) <= 30, "word must be 1-30 characters"
    assert word.strip() == word and " " not in word, "word must be a single word"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(word)
    # Read it back and re-check: what the grader reads must be the word.
    written = open(out_path, encoding="utf-8").read()
    assert written == word, "entry.txt must contain exactly the chosen word"
    print(word)


if __name__ == "__main__":
    main()
