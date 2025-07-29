2025-04-21
# Epistemic Limits of Computation


Kurt Gödel, in his Incompleteness Theorems, states that an expressive formal system cannot be both consistent and complete at the same time. This leads to some unintuitive consequences, such as the existence of true statements that cannot be proven within the system, or that a system cannot prove its own consistency.

It is possible to construct such statements as: "I am not provable in this system." This statement leads to a paradox: if we could prove it, we would contradict its own message, and if we cannot prove it, then it is true, which again contradicts the assumption that it is unprovable. As so, we conclude that the statement is true but unprovable.

A famous example in computer science is Turing's Halting Problem. Suppose we have access to a program that checks whether a given program halts or not. What happens if we create a new program with a twist: if the input program halts, the new program forces it to run forever. And if the input program does not halt, it forces it to stop, and then we run this new program on itself? This leads to a paradox caused by self-reference: the program halts if and only if it does not halt.

The same problem arises in literature in one of the dialogs of "Gödel, Escher, Bach: an Eternal Golden Braid" from Douglas Hofstadter , where, when confronted by a genie offering three wishes, Achilles says: "I wish my wish would not be granted.". A comparable dilemma arises in Don Quijote de la Mancha from Cervantes, when Don Quixote was required to make a statement to cross the bridge and enter a town. If the statement was false, he would be hanged, and if it was true, he would be to pass freely. He then said: "I will be hanged." making it impossible to determine whether he should be hanged or not. 


![cube](/img/cube.png)

Consider we have a special Rubik's Cube where, instead of colors, it has text written on it: "This cube is not solvable". When shuffled, the cube appears mixed up and unsolved. However, when we attempt to put it back to its original state, we realize that it is impossible to solve. The cube itself claims that it is unsolvable. As so, assuming that the rules of the Rubik's Cube are consistent, "solving it" cannot happen. There are no valid moves that lead to a solved state.

This means that the statement "This cube is not solvable" is actually true. We arrive at a true but unprovable statement, because the only way to prove it would be to attempt solving the cube, and impossible task due to its very nature.


With this, Gödel showed that there are **epistemic limits of the universe**, things that not even a genie or computer can prove. I'm not sure if it is our limits or the universe's, but it is a fundamental limitation as we cannot automatically verify every property, such as the absence of errors, halting, or other undecidable problems. Therefore, no analysis tool can be both complete and effective for all programs.
