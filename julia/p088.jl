using Primes
using StrLiterals, StrFormat
using DataStructures

a = [1, 2, 3]

reduce(*, a)

function check_prod_sum(a::Vector{T}, k::Int) where {T<:Number}
    return sum(a)==reduce(*, a) && length(a)==k
end  # function check_prod_sum

check_prod_sum(a, 3)

function all_factorizations(n::Int)
    res = Set{Vector{Int}}()
    
    function factorize!(v::Vector{Int}, num::Int)
        if num==1
            # println(f"v = \(v), num = \(num)")
            push!(res, sort(v))
            return
        end
        for d=num:-1:2
            if num%d == 0
                q = floor(Int, num/d)
                push!(v, d)
                factorize!(v, q)
                pop!(v)
            end
        end
    end

    factorize!(Int[], n)

    return res

end  # function all_factorizations


a = all_factorizations(12)



# function min_prod_sum(k::Int)
#     num = 0
#     for num = (k+1):2k

#     end

    
#     return num
# end  # function min_prod_sum

function p88(K::Int=12)
    min_prod_sum_num = SortedDict{Int, Int}()
    found = fill(false, K)
    found[1] = true
    for k=4:2K
        fs = all_factorizations(k)
        for f in fs
            l = length(f)
            l < 2 && continue
            n = k - sum(f) + l
            if n <= K && !found[n]
                found[n] = true
                min_prod_sum_num[n] = k
            end
        end
        all(found) && break
    end
    # @show min_prod_sum_num
    # for kv in min_prod_sum_num
    #     println(kv)
    # end
    return sum(Set(values(min_prod_sum_num)))
end  # function p88

@time p88()

# 2 seconds
@time p88(12000)
