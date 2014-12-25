> import Data.Array
> import Data.List
> import Data.Ord (comparing)


> chain :: Integer -> [Integer]
> chain 1 = [1]
> chain n
>   | even n    = n : chain (n `div` 2)
>   | odd n     = n : chain (3*n + 1)
>
> l n = length $ chain n

calculating chain lengths by memoization
not clear to me how it is handling new numbers less than n
for which it does not know the chain length

> chainLengths n = a
>   where a = listArray (1,n) $ 1:[chainLen n x | x <- [2..n]]
>         chainLen n x = if x' <= n then 1 + (a ! x') else 1 + chainLen n x'
>                        where x' = if even x then x `div` 2 else 3*x + 1
>
> main = putStrLn $ "PE14 Ans: " ++ show a
>       where a = fst $ maximumBy (comparing snd) $ assocs $ chainLengths $ 10^6

assocs returns the array as a list of tuples (i, e)
