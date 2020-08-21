function d(n::Int)
    n==1 && return 0
    n==2 && return 1
    res = 1 # include 1 here and then no need to worry about n
    sqrta = ceil(Int, sqrt(n))
    for a in 2:(sqrta-1)
        q, r = divrem(n, a)
        if r==0
            res += a + q
        end
    end 
    if sqrta*sqrta == n
        res += sqrta
    end 
    res
end # function d

function sum_of_amicable_numbers_below(n::Int=10_000)
    D = [d(i) for i in 1:n]
    res = 0 
    @inbounds for a in 1:n 
        b = D[a]
        if a != b && 1 ≤ b ≤ n && a == D[b]
            res += a
            # println(a)
        end 
    end 
    println("p21: $res")
    res
end

@time sum_of_amicable_numbers_below(10_000)

@time sum_of_amicable_numbers_below(100_000)


