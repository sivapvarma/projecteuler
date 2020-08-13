function f_fact(N::T) where {T <: Union{Int, BigInt}}
    fac = factorial(N)
    # while fac % 10 == 0
    #     fac = T( fac // 10 )
    # end
    fac = remove_trail_zeros(fac)
    return fac % 100000
end

# function f(N::Integer)
#     fac = n = 1
#     while n <= N
#         fac = ( fac * n )
#         while fac % 10 == 0
#             fac = Integer( fac // 10 )
#         end
#         fac = fac % 100000
#         n += 1
#     end
#     return fac % 100000 
# end

function f(N::T) where {T <: Union{Int, BigInt}}
    fac = n = 1
    while n <= N
        fac = fac * n
        fac = remove_trail_zeros(fac)
        fac = fac % 10000000
        n += 1
    end
    return fac % 100000 
end

print("f(20) = $(f(20))")
print("f(20) = $(f_fact(20))")

cnt = 0
for num in 1:1000
    # println("f($num) = $(f(num))\t\t$(f_fact(big(num)))")
    gt = f_fact(big(num))
    res = f(num)
    global cnt
    if gt != res
        println("f($num) = $res != f_fact($num) = $gt")
        cnt += 1 
    else
        println("f($num) = $gt \t\t$res")
    end
end
println("$cnt results wrong.")

function remove_trail_zeros(n::T) where {T<:Union{Int,BigInt}}
    while n % 10 == 0
        n = T(n // 10)
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