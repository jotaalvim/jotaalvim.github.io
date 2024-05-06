2024-05-06
# Going Monadic



https://github.com/jotaalvim/jotaalvim-tools/blob/main/ddf/del.hs

This is tutorial explains how to make a script to remove duplicated files in a directory in Haskell.
As so this program was written as an introduction to **monadic  programming**. 


I'm going to use **md5 hash** do compare each file. This means that files with the same md5 have the the same content and so are duplicated.

```haskell
md5 :: ByteString -> Digest MD5
md5 = hash
```

A ByteString is a binary string, it's a block of memory with the file content, this function receives a file content (in bytestring form) and hash's it.


Lets read a file content with  ```readFile :: FilePath -> IO ByteString ``` a function that takes a String (FilePath) and returns the binary content of a file inside an IO. To escape  IO we can use left arrow ``` <- ``` . This arrow decapsulate the things inside IO. In this example : 
```  (content <- readFile fp)  ``` content is not of type IO ByteString but ByteString. 

I'll return a pair of the file's name and it's hash:
```haskell
makeHash :: FilePath -> IO (FilePath, Digest MD5) 
makeHash fp = do
	content <- readFile fp
	return (fp, md5 content)
```

Assuming I apply this function to every file in a directory I can find which files are duplicated by comparing the second element of each pair (hash).


Algorithmically finding duplicated items in a list is equivalent to substrancting ( \\\\ - list subtraction ) to the original list,  the same list  but without duplicates:
```haskell
duplicated l = l \\ nubBy (\(_,b)(_,d) -> b == d) l
```

<details>
  <summary> a more interesting way to define duplicated </summary>
		There's one combinator that allow us to make this function pointfree and it's the bind >>=.
	```haskell
	duplicated = nubBy (\(_,b)(_,d) -> b == d) >>= flip (\\)
	```
		It might not make sence but here's a simple definition of bind that does not use monadic power, this makes it possible to rearrange the inputs we pass to numBy and (\\).
	```haskell
	(>>=) :: (a -> b) -> (b -> a -> c) -> a -> c
	f >>= k = \ r -> k (f r) r
	```
</details>


The next step is to map makeHash to every element of a directory.
Suppose we have a list of strings that are file paths, to map them to makeHash means to produce a list with IO inside  because ``` makeHash :: FilePath -> IO (FilePath, Digest MD5) ```

```
ghci> :t map makeHash
map makeHash :: [FilePath] -> [IO (FilePath, Digest MD5)]
```

That's getting weird, We need to traverse the list and swap the IO monad with the List so that we produce the more intuitive ``` IO [(FilePath, Digest MD5)] ```. You can read that type as "a side effect that produces Lists of pair of filepath and it's hash". 

The way to this is with the sequence functions, it swaps 2 nested monads!
```
ghci> :t sequence
sequence :: (Traversable t, Monad m) => t (m a) -> m (t a)   
```

This way we produce the final result

```
ghci> :t sequence . map makeHash
sequence . map makeHash :: [FilePath] -> IO [(FilePath, Digest MD5)] 
```


