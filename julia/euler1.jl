s = sum( filter( x -> ((x%3==0) | (x%5==0)), [1:999] ) )
println(s)
