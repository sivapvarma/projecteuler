using Combinatorics
using DataStructures

A6 = [11, 17, 20, 22, 23, 24 ]

a7 = [22]
for n in A6
    push!(a7, n + 22)
end

a7

sum(a7)

join(map(x->string(x), a7))


l = A6


A6 = [11, 7, 20, 22, 23, 24 ]
sums_list = DefaultDict{Int, Bool}(false)
sums = [(Inf, -Inf) for _ in 1:5]
for sset in powerset(A6, 1, 5)
    println(sset)
    x = sum(sset)
    sums_list[x] = !sums_list[x]
    y = length(sset)
    a, b = sums[y]
    if x > b
        b = x
    end
    if x < a
        a = x
    end
end

all(values(sums_list))

a6 = Set(A6)

for s in powerset(A6, 1, 5)
    println(s)
end

ssets = collect(powerset(A6, 1, 5))

for (a,b) in combinations(A6, 2)
    println("$a, $b")
end


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


a6 = [11, 17, 20, 22, 23, 24]
check_subsets(a6)
sum(a6)
a6 = [11, 18, 19, 20, 22, 25]
check_subsets(a6)
sum(a6)
a6 = [9, 18, 19, 20, 22, 25]
check_subsets(a6)
sum(a6)


A6 = [11, 18, 19, 20, 22, 25]
check_subsets(A6)
a7 = [20]
for n in A6
    push!(a7, n + 22)
end

a7


minsum = sum(a7)
options = []
function generate_options(l, ds, idx)
    len = length(l)
    if idx > len
        global minsum
        if sum(l) >= minsum
            return l
        end
        if check_subsets(l)
            minsum = sum(l)
            push!(options, l)
            println(l)
        end
        return l
    end
    for (i, v) in enumerate(ds)
        l[idx] += v
        generate_options(l, ds, idx + 1)
        l[idx] -= v
    end
end

generate_options(a7, -3:3, 1)

options

r = options[1]

sum(r)