using Combinatorics

disjoint(a, b) = a ∩ b == []

function check_subsets(l::Vector{Int})
    len = length(l)
    pset = collect(powerset(l, 1, len-1))
    for (a, b) in combinations(pset, 2)
        if disjoint(a, b)
            sa, sb = sum(a), sum(b)
            sa == sb && return false
            la, lb = length(a), length(b)
            la > lb && sa <= sb && return false
            la < lb && sa >= sb && return false
        end
    end
    return true
end

