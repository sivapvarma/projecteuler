using CSV
using LightGraphs
using GraphPlot
using Plots
unicodeplots()
using TikzGraphs

nums = []
for r in CSV.File("../data/p079_keylog.txt"; header=["n"], type=String)
    println(r.n)
    push!(nums, r.n)
end


nums

ds = "1234567890"
vlabel = Dict(k=>v for (k, v) in enumerate(ds))
labelv = Dict(v=>k for (k, v) in vlabel)

G = SimpleDiGraph(10)
for n in nums
    println(n)
    add_edge!(G, labelv[n[1]], labelv[n[2]])
    add_edge!(G, labelv[n[1]], labelv[n[3]])
    add_edge!(G, labelv[n[2]], labelv[n[3]])
    # for e in edges(G)
    #     @show e
    # end
    # break
end

G

TikzGraphs.plot(G)

gplot(G, layout=circular_layout, nodelabel=sort(collect(values(vlabel))), nodesize=0.5)

bfs_tree(G, 1)

#######
## Final Solutions
#######

using DataStructures
using DelimitedFiles

logins = readdlm("../data/p079_keylog.txt", String)

function p079()
    digits_after = DefaultDict(Set)
    for login in logins
        push!(digits_after[login[1]], login[2:3]...)
        push!(digits_after[login[2]], login[3])
        push!(digits_after[login[3]], "")
    end
    join(map(t -> t[2], sort([(length(v), k) for (k,v) in digits_after], rev=true)))
end  # function p079

# 0.228345 seconds (324.58 k allocations: 17.000 MiB, 7.13% gc time)
# "73162890"
@time p079()