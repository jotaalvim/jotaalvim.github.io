2025-08-01
# Can Debuggers Think Like Humans? Abstract Debugging

Can abstract debugging be more expressive, and therefore not only superior to traditional debugging, but also lead to a deeper understanding of program behavior?

Typically debuggers are of a somewhat rudimentary nature. There are a lot of varieties of them, traditional debuggers allow developers to step through the execution of a program and inspect the contents of variables. If the person does not find the bug in the first few steps, they may have to restart the process with different inputs and values. Other techniques such as **Multiverse Debugging**, uses a brute-force like approach. It explores the space of possible values in a controlled manner. This technique explores altering values at key decision points in our programs. Or even **Concolic debugging**, a hybrid of concrete and symbolic execution. In contrast to random testing, concolic execution uses symbolic reasoning to find the values that split the execution paths. It allows for exploring multiple execution scenarios more efficiently than pure brute force and is very useful in debugging non-deterministic programs. However, these approaches have a few drawbacks. Computing power is still not enough to tackle complex problems, and human ability to effectively utilize these tools remains a bottleneck.  


Instead of relying solely on trial and error or brute force, suppose we adapted a debugger to mimic how humans think and make sense of complex problems. A good example of a real-world hard problem is chess. Chess players cannot analyze all possible positions, so to bridge this gap, they study positional concepts and principles and rules that help them understand the game better. While computers can evaluate millions of positions per second, humans rely on abstractions and heuristics to make decisions. Computers can tell us whether a move is good or bad and provide a long sequence of moves to justify it. But humans need some kind of abstraction or rule of thumb to understand why a move is good or bad.

Similarly, [Abstract Debuggers](https://dl.acm.org/doi/10.1145/3689492.3690053) enable developers to explore abstract program states and reason with assumptions that apply to all possible executions of a program. Abstractions allow us to consider entire categories chunks of behaviors rather than individual execution paths. Abstract debugging shifts the perspective toward reasoning about program behavior based on its abstraction and over-approximations of the program's behavior. Which contrasts with common debuggers, which show results from the executions that are run.


Is this technique actually better for refining hypotheses about programs by exploring the results of all possible execution paths? 


One may argue that abstract debuggers are wrong as they may reach a somewhat incorrect results due to over-approximations. We might reach an abstraction that is impossible to reach on the concrete original program. Even if "wrong" I believe that they're still useful because humans still find meaning in "incorrect" things such as analogies. Even quantum-mechanics, besides ultra precise prediction does not vividly correspond to nature, and still people use it.

One may argue that abstract debuggers are flawed because they can produce somewhat incorrect results due to over-approximations. We might reach an abstraction that is impossible to reach in the original concrete program. Even if they are "wrong", I believe they are still useful, because humans often find meaning in "incorrect" things, such as analogies. Even quantum mechanics, despite its ultra-precise predictions, does not vividly correspond to nature, and yet people continue to use it.
