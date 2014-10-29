euler1 n = sum[x | x <- [1..n-1], mod x 3 == 0 || mod x 5 == 0]
main = print (euler1 1000)
