2024-02-04
# Is it feasible to create the List Monad in Scratch?

Sometimes the idea of doing unuseful and hard things excites me, implementing the [list monad](https://en.wikibooks.org/wiki/Haskell/Understanding_monads/List) in [scratch](https://scratch.mit.edu/) was one of those. Scratch already has implemented the List datatype making our lives easier.


To make things simple, I'll only create four functions to implement the list monad:


* ``` return :: a -> [a] ```  for injecting a value into a list
* ``` map :: (a -> b) -> [a] -> [b] ```  for applying a function to all elements of a list
*  ``` join :: [[a]] -> [a] ``` for grouping nested monads (lists in this case)
*  ``` bind :: [a] -> (a -> [b]) -> [b] ``` for concatenating the results of applying a function to each element of a list

## Scratch
Doing things in Scratch is a difficult challenge. Concepts we have taken for granted in other languages do not exist in scratch. Besides actually implementing the list monad, I had to collaborate with the fact that there's:

* No higher order and no function pointers
* No return statements
* Only static variables

To my surprise, there's already a very similar programming language, Assembly!

## Dealing with return statements
Let's analyze the function successor written in c (left), which is implemented in assembly (right).
![bit](/img/assembly-succ.png)

We can see that it uses the auxiliary registry EAX to "return" the result. This means the function that is calling succ will assume the result is going to end up stored in the EAX variable. So creating an EAX variable in Scratch with the same purpose seems reasonable.

Here is the definition of successor, predessecor, and identity function in scratch:
![bit](/img/scratch-succ.png)


## Solving  higher order
New problems start to emerge when I want to apply a specific function without being hardcoded. This means that the definition of map is going to be the same regardless of the function for which I want to map each element.

I can't pass functions as arguments in scratch, but I can pass strings. I created a function with the sole purpose of running and applying arguments to functions. To simplify, I'm only using functions of ariety 1, and I have to manually insert them here:

![bit](/img/scratch-apply.png)

## Map
To map each element, I'm assuming there's already content in a list registry. Because there's no return statement, after applying the function to each element, I have to get back the result from EAX.
![bit](/img/scratch-map.png)


## Join
I don't know if it's possible to make a concat operation because when I can't iterate a nested list, I don't know how many elements there are, so I may have to make my own length function.
## Bind

## Use cases