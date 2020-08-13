function check_anagram(s1, s2)
    if length(s1) != length(s2)
        return false
    end
    d1 = join(sort(collect(s1)))
    d2 = join(sort(collect(s2)))
    return d1 == d2
end

function to_dict(s)
    d = Dict(l => 0 for l in 'A':'Z')
    for c in s
        d[c] += 1
    end
    return d
end

function anagram_pairs()
    for i in 1:length(words)
        for j in i+1:length(words)
            if check_anagram(words[i], words[j])
                produce((words[i], words[j]))
            end
        end
    end
end

function test()
    for i in 1:10
        produce(i)
    end
    produce(-1)
end

f = open("../data/p098_words.txt")
lns = readlines(f)
close(f)
words = map(x -> strip(x, ['\"', '\\']), split(strip(lns[1]), ','))
println("$(length(words)) words.")
lns = map(x -> length(x), words)
println("length of the longest words is $(maximum(lns))")
# sort by length of words
sort!(words, by=length, rev=true)
# p = Task(anagram_pairs(words))
# pairs = collect(p)
# println("$(length(pairs)) pairs.")
p = Task(anagram_pairs)
pairs = collect(p)
for x in pairs
    # if x < 0
    #     break
    # end
    println("$x")
end
println("$(length(pairs)) pairs.")

function is_square(x::Integer)
    k = round(Int, sqrt(x))
    if k*k != x
        return false
    end
    return true
end


function anagram_squares()
    for i in 1:length(sqs)
        for j in i+1:length(sqs)
            if check_anagram(sqs[i], sqs[j])
                produce((sqs[i], sqs[j]))
            end
        end
    end
end

# longest anagram has nine characters. I just have to match them now
squares = [x*x for x in 1:round(Int, sqrt(10^10))]
sqs = map(x->string(x), squares)
println("Computing square pairs...")
# q = Task(anagram_squares)
# square_pairs = collect(q)
# println("$(length(square_pairs)) square pairs.")
# for x in square_pairs
#     println("$x")
# end

function anagrams(wordlist)
    hash = Dict()
    for word in wordlist
        ws = join(sort(collect(word)))
        hash[ws] = [get(hash, ws, []); word]
    end
    collect(values(filter((x,y)->length(y)>1, hash)))
end

sqgrams = anagrams(sqs)

using Combinatorics

function mach(wpairs, numgrams)
    r = []
    for p in wpairs
        for i in 1:length(numgrams)
            if length(numgrams[i][1]) != length(p[1])
                continue
            end
            for np in permutations(numgrams[i], 2)
                if match_pairs(p, tuple(np...))
                    r = [r; (p, np)]
                end
            end
        end
    end
    return r
end

function match_pairs(p, np)
    d = Dict(k => v for (k, v) in zip(collect(p[1]), collect(np[1])))
    if length(d) != length(unique(collect(values(d))))
        return false
    end
    for (k, v) in zip(collect(p[2]), collect(np[2]))
        if d[k] != v
            return false
        end
    end
    return true
end
println("Computing associations between squares and anagrams from list.")
r = mach(pairs, sqgrams)
println("Computing the answer...")
n = 0
w = ()
for k in r
    n = max(n, parse(Int, k[2][1]))
    n = max(n, parse(Int, k[2][2]))
    ns = string(n)
    if ns == k[2][1] || ns == k[2][2]
        w = k[1]
    end
end
println("PE98 Ans: $n")
println("Corresponds to $w")