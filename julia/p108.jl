function nreciprocals(n::Integer)
    r = 1
    yl = n*(n+1)
    for x in n+2:2n
        for y in yl:-1:2n
            if n*(x+y) == x*y
                r += 1
                yl = y
                break
            end
        end
    end
    return r
end

function reciprocals_list(n::Integer)
    rs = [(n+1, n*(n+1))]
    yl = n*(n+1)
    for x in n+2:2n
        for y in yl:-1:2n
            if n*(x+y) == x*y
                rs = [rs; (x, y)]
                yl = y
                break
            end
        end
    end
    return rs
end

function nreciprocals_limit(l::Integer)
    i = 2
    l1 = 1
    while true
        # n = length(reciprocals_list(i))
        n = nreciprocals(i)
        # println("$i: $n")
        if n > l
            println(">$l  $i: $n")
            break
        elseif n > l1
            println(">$(l1)  $i: $n")
            l1 *= 10
        end
        i += 1
    end
    return i
end

function nreciprocals_list_limit(l::Integer)
    i = 2
    l1 = 1
    while true
        # n = length(reciprocals_list(i))
        n = nreciprocals(i)
        println("$i: $n")
        if n > l
            println(">$l  $i: $n")
            break
        elseif n > l1
            println(">$(l1)  $i: $n")
            l1 *= 10
        end
        i += 1
    end
    return i
end

@time nreciprocals_limit(10)
@time nreciprocals_limit(10)
# @time nreciprocals_limit(100)
# @time nreciprocals_limit(1000)
# @time nreciprocals_list_limit(10)
# @time nreciprocals_list_limit(10)
using Primes

println("Computing primes(10)...")
@time primes(10)
println("Actual primes() run...")
@time const ps = primes(2*3*5*7*11*13*17*19)

function nrs(n::Integer, ps::Array{Int64, 1})
    n2ds = 1
    for p in ps
        e = 0
        while n%p == 0
            n = div(n, p)
            e += 2
        end
        n2ds *= e+1
        if n == 1
            break
        end
    end
    return div(n2ds+1, 2)
end

function nrs_list(l::Integer)
    i = 1
    while true
        n = nrs(i, ps)
        println("$i: $n")
        if n > l
            println(">$l $i: $n")
            break
        end
        i += 1
    end
    return i
end

@time nrs_list(10)
@time nrs_list(10)
@time nrs_list(100)
@time nrs_list(1000)
@time nrs_list(10000)