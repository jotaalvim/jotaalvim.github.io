2024-02-04
# Is it possible to implement the List Monad in Scratch?

Sometimes the idea of doing unusefull and hard things excites me, implementing the [list monad](https://en.wikibooks.org/wiki/Haskell/Understanding_monads/List) in [scratch](https://scratch.mit.edu/) was one of those. 


For sake of simplicity, to implement the list monad I going to define 4 different functions:


* ``` return :: a -> [a] ```  for injecting a value into a list
* ``` map :: (a -> b) -> [a] -> [b] ```  for aplllying a function to all elements of a list
*  ``` join :: [[a]] -> [a] ``` for grouping nested monads (lists in this case)
*  ``` bind :: [a] -> (a -> [b]) -> [b] ``` for concatenating the results of applying a function to each element of a list

## Scratch 
Doing thigs in Scratch is a difficult challenge because concepts we have for granted in other languages do not exits in scratch. Besides actually impleting the list monad