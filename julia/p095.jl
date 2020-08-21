function d(n::Int)
    n==1 && return 0
    n==2 && return 1
    res = 1 # include 1 here and then no need to worry about n
    sqrta = ceil(Int, sqrt(n))
    for a in 2:(sqrta-1)
        q, r = divrem(n, a)
        if r==0
            res += a + q
        end
    end 
    if sqrta*sqrta == n
        res += sqrta
    end 
    res
end # function d


function p95(L::Int=10^6)
    @show L
    D = [d(i) for i in 1:L]
    res = 0
    max_len = -L
    seen = fill(false, L)
    chains = Vector{Vector{Int}}()
    for i in 1:L
        if !seen[i]
            seen[i] = true
            ch = Int[]
            flag = false
            @inbounds while 1 ≤ D[i] ≤ L
                # @show i
                # @show ch
                push!(ch, i)
                i = D[i]
                # seen[i] = true
                if i == ch[1]
                    flag = true
                    break
                elseif i in ch
                    break
                end
            end
            if flag
                @show ch
                push!(chains, ch)
                for k in ch
                    seen[k] = true
                end
                if length(ch) > max_len
                    max_len = length(ch)
                    res = minimum(ch)
                end
            end
        end
    end
    println("p95: $res")
    res
end


@time p95(1000)

@time p95()

d(6)