using Combinatorics

const opers = [:+, :-, :*, :/]

function eval_exprs(t::Vector{Int})
    res = [] 
    # exprs = []
    a, b, c, d = t
    for (o1, o2, o3) in Iterators.product(opers, opers, opers)
        e1 = Meta.parse( "$a $o1 (($b $o2 $c) $o3 $d)" )
        e2 = Meta.parse( "$a $o1 ($b $o2 ($c $o3 $d))" )
        e3 = Meta.parse( "($a $o1 $b) $o2 ($c $o3 $d)" )
        e4 = Meta.parse( "(($a $o1 $b) $o2 $c) $o3 $d" )
        e5 = Meta.parse( "($a $o1 ($b $o2 $c)) $o3 $d" )
        ev = eval(e1)
        push!(res, ev)
        # @show e1 ev
        ev = eval(e2)
        push!(res, ev)
        # @show e2 ev
        ev = eval(e3)
        push!(res, ev)
        # @show e3 ev
        ev = eval(e4)
        push!(res, ev)
        # @show e4 ev
        ev = eval(e5)
        push!(res, ev)
        # @show e5 ev
        # push!(res, eval(e2))
        # push!(res, eval(e3))
        # push!(res, eval(e4))
        # push!(res, eval(e5))
    end
    # println(length(res))
    ret = Int[]
    for (i, v) in enumerate(res)
        # println("$i, $v, $(typeof(v))")
        if v > 0 && isapprox(rem(v, 1), 0, atol=1e-2)
            push!(ret, round(Int, v))
        end
    end
    return unique(ret)
end  # function eval_exprs

eval_exprs([4, 2, 3, 1])

function findn(a::Vector)
    isempty(a) && return 0
    a[1] != 1 && return 0
    for i in 2:length(a)
        if i != a[i]
            return i-1
        end
    end    
    return length(a)
end  # function findn

function check(t::Vector{Int})
    a = []
    for tx in permutations(t)
        # @show tx typeof(tx)
        vals = eval_exprs(tx)
        append!(a, vals)
    end
    a = unique(a)
    sort!(a)
    # @show a
    n = findn(a)
    st = join(map(string, sort(t)))
    return n,st
end  # function check

check([1, 2, 3, 4])


function p93()
    ds = collect(1:9)
    maxn, res = -10, ""
    for (i,t) in enumerate(combinations(ds, 4))
        @show i
        n, st = check(t)
        if n > maxn
            maxn = n
            res = st
        end
    end
    println("p93: $res $maxn")
end # function p93


# p93: 1258 51
# 194.718024 seconds (65.77 M allocations: 3.838 GiB, 0.17% gc time)
@time p93()


a = collect(1:3)

for (i, t) in enumerate(combinations(a, 2))
    println("$i: $t")
end