function is_reversible(n::Int)
    n%10==0 && return false
    nr = parse(Int, reverse(string(n)))
    odds = Set("13579")
    ds = Set(string(nr + n))
    return ds ⊆ odds
end  # function is_reversible

function p145(limit::Int = 10^9)
    res = []
    for i=1:limit
        if is_reversible(i)
            push!(res, i)
        end
    end
    num = length(res)
    # @show res
    println("$num reversible numbers below $limit.")
end  # function p145

@time p145(1000)

# 682.568039 seconds
@time p145()