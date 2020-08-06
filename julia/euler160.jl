function f_fact(N::Integer)
    fac = factorial(big(N))
    while fac % 10 == 0
        fac = BigInt( fac // 10 )
    end
    return fac % 100000
end

function f(N::Integer)
    fac = n = 1
    while n <= N
        fac = ( fac * n )
        while fac % 10 == 0
            fac = Integer( fac // 10 )
        end
        fac = fac % 100000
        n += 1
    end
    return fac % 100000 
end

print("f(20) = $(f(20))")
print("f(20) = $(f_fact(20))")


for num in 1:10000
println("f($num) = $(f(num))\t\t$(f_fact(num))")
end

function remove_trail_zeros(n::Integer)
    while n % 10 == 0
        n = Integer(n // 10)
    end
    return n
end

function f_105(res::Int)
    n = 1
    while n < 10^5
        res = res * n
        res = remove_trail_zeros(res)
        res = res % 10^5
        n += 1 
    end
    return res
end


for num in 10^5:10^5+30
    println("f($num) = $(f(num))")
end


function f_new(N::Integer)
    if N <= 10^5
        return f(N)
    end
    res = f_105(1)
    n = 10^5
    while n <= N
        res = f_105(res)
        n += 10^5
    end
    return res
end

for num in 10^5:10^5:10^6
    println("f($num) = $(f(num))\t\t$(f_new(num))")
end