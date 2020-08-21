using StrLiterals, StrFormat
using LightGraphs
using MetaGraphs
using Plots
using GraphRecipes
gr()
using Combinatorics


a = Set([Set([1, 2]), Set([12, 3])])

b = Set([Set([12, 3]), Set([1, 2])])

a == b

c = Set([a, b])


for i=1:9
    s = f"\%02d(i^2)"
    println()
end

squares = [f"\%02d(i^2)" for i in 1:9]




G = SimpleGraph()

add_edge!(G, 0, 1)

g = Graph()

add_edge!(g, 0, 1)

parseint(x::Char) = parse(Int, x)
parseint(x::String) = parse(Int, x)

g = SimpleGraph(10)
for sq in squares
    x, y = [parseint(t) for t in sq]
    println("$x, $y")
    add_edge!(g, x+1, y+1)
end

add_edge!(g, )

nv(g)
ne(g)


p = graphplot(g,
          names=[string(x) for x in 0:9],
          dpi=150,
          nodesize=0.3,
          method=:circular,
          nodeshape=:circle,
          nodecolor=:lightgrey)

x = 4

for v in vertices(g)
    println(v)
end


G = MetaGraph(g)

for v in vertices(G)
    set_prop!(G, v, :name, string(v))
end

q = 0


# this problem is simply the bipartite matching, and the counting 
# the number of possibilities for redundancies.


# infact this problem is much simpler.
# note 49 == 46 == 64

function valid(c1, c2, sq)
    all( (x in c1 && y in c2) || (x in c2 && y in c1) for (x,y) in sq )
end # function valid

function p90()
    squares = [(0, 1), (0, 4), (0, 6), (1, 6), (2, 5),
               (3, 6), (6, 4), (8, 1)]
    faces = collect(0:9)
    faces[10] = 6
    combs = collect(combinations(faces, 6))
    res = 0
    for (i, c1) in enumerate(combs)
        for c2 in combs[begin:i-1]
            res += valid(c1, c2, squares)
        end
    end
    println("p90: $res")
    res
end  # function p90

# 1217
@time p90()

squares = [(0, 1), (0, 4), (0, 6), (1, 6), (2, 5),
           (3, 6), (6, 4), (8, 1)]
valid([0, 5, 6, 7, 8, 9], [1, 2, 3, 4, 6, 7], squares)