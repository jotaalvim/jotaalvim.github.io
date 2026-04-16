2026-04-17
# What even is a Programming Language

The essence of a programming languages is quite unique in contrast to a natural language. Programming Languages (PLs) are seen as an interface for humans to talk to the machine. Their vocabulary is reduced to a minimum, and they are made so that each symbol does not have ambiguity in its meaning, making it reliable.

As a software developer, I have always taken languages very seriously. It fascinates me that many people have a clear opinion on what languages are, yet the concept of a language is somewhat fuzzy. I find statements like these, ["Linguists believe that there are 297 living languages in China today"](https://www.worldatlas.com/articles/what-languages-are-spoken-in-china.html) very strange, because languages are not rigid. We interchange words and sounds, and sometimes a language is a subset of a bigger one. I wonder how one can count and fully distinguish them.

This strange feeling also applies to programming languages. To my surprise, many developers use rules and heuristics to completely separate a programming language from others. But some of their rules are too rigid, as they don't include edge cases and ultimately fail to define what makes a language be about programming.

Sometimes people say that `xml`, `json`, `html`, `markdom` are not PL because they "don't do anything". By this, they usually mean those languages are not expressive enough, and that the context where they're used isn't generic enough to make them be categorized as PL. On the other hand,`Python`, `C`, `Go`, `Haskell` are of general purpose PL because they can do "everything". 

Which makes me ask yet another question: **what does everything mean, and what makes a language generic?** Do they need a mechanism to represent algebraic data types such as lists, products, and sums? Does it have to be Turing complete, meaning it can perform any computation that a computer can? Does it even need to be compilable and have an abstract syntax tree?

I attempted to answer those questions by looking at some of its features and characteristics but got nowhere. In [Lambda Calculus](https://en.wikipedia.org/wiki/Lambda_calculus) numbers, strings, and structs are not intrinsically represented in the language, and it's considered general. In CSS the concept of [Inheritance](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming)) exists, but it's not universally accepted to be a general language. [Alloy](https://alloytools.org/) is used to model and find structural holes in our application logic, making it easier to understand what logical predicates are needed. However, it does not have the capability to do numeric arithmetic, as it does not even have numbers. We could explore more characteristics like compositions, but i don't think this will reveal the necessary conditions for a language to be considered general purpose.

So I tried instead to think of tasks that only a truly general PL can do. I came up with the calculation of prime numbers. Surprisingly, **this task might not be generic enough** because of an interesting corner case: [regular expressions](https://en.wikipedia.org/wiki/Regular_expression). This domain specific language serves the purpose of matching patterns in text. The following odd regular expression `^.?$|^(..+?)\1+$` matches strings whose length is a composite number (not prime).

In the following example, each line number corresponds to its length. Strings with a prime number of characters long do not appear highlighted!

![vscpde](/img/vscode.png)

What a curious example this unusual approach to finding prime numbers is. If calculating prime numbers is not something only a truly general PL does, I wonder what kinds of tasks make people consider a PL general? 

Perception plays a large role, the following meme, while analogous, underlines an important fact.

![fish meme](/img/fish_meme.png)

"Wet" refers to the presence of moisture or liquid, and "dry" to the absence of it. Both the person and the fish fail to realize that the **context of "wet" and "dry"is very specific** and not generic at all. Does this concept only apply to seawater, or can it be extended to distilled water or any other liquids? An interesting piece of information appears in [Is glass liquid or solid?](https://www.desy.de/user/projects/Physics/General/Glass/glass.html), where the authors conclude that there is not a clear definition of the distinction between solids and highly viscous liquids. Hypothetically, assuming we included any other liquids in the "wet" definition, to someone whose context is that he lives surrounded by a solid would also be able to argue that both the fish and the human are dry.

Hidden contexts are everywhere, in P.L maybe it's the runtime environment or the compiler. The question of what counts as a programming language is very amusing but overall irrelevant. In the previous example, it's astonishing how that regular expression achieves the behavior above. And I consider it, on some abstract level, generic. All programming languages are encapsulated in some specific context. In practice, I like to think of languages like `json` as genuine programming languages whose semantic action is nonexistent. Statements like "they don't do anything" are in a way fallacious because we're probably assuming and missing out on some context. The hard part is drawing the line separating the specific from a generic context, directly echoing an interesting thought of Hofstadter:

> “This idea that there is generality in the specific is of far-reaching importance.” ― Douglas R. Hofstadter

