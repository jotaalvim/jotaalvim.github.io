2025-04-21
# Limits of Computation

G\"{o}del, in his Imcompletness Theorem states that there exist true statements that cannot be proved. Let's explore this theorem with a simple example.

![cube](/img/cube.png)

Consider we have a special Rubik's Cube where, instead of colors, it has text written on it: "This cube is not solvable". When shuffled, the cube appears mixed up and unsolved. However, when we attempt to put it back to its original state, we realize that it is impossible to solve. The cube itself claims that it is unsolvable. As so, assuming that the rules of the Rubik's Cube are consistent, "solving it" cannot happen. There are no valid moves that lead to a solved state.

This means that the statement "This cube is not solvable" is actually true. We arrive at a true but unprovable statement, because the only way to prove it would be to attempt solving the cube, and impossible task due to its very nature.

G\"{o}del's theorem does not say that being consistent is impossible, because it is, however, it comes at the cost of incompleteness.

His interesting ideas can be applied to computer science as well, as there are problems that we cannot solve. One famous example is the Halting Problem, which is undecidable. It is impossible to construct a general algorithm that determines whether an arbitrary program will eventually halt or run forever.

This is a fundamental limitation, as we cannot automatically verify every property, such as the absence of errors, halting, or other undecidable problems. No analysis tool can be both complete and effective for all programs.
