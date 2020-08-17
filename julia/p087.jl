include("euler.jl")

function p87(N::Int)
    limit = ceil(Int, sqrt(N))
    primes = eratosthenes(limit)
    res = Set{Int}()
    for a=primes
        an = a^4
        an > N && break
        for b=primes
            bn = b^3
            bn > N && break
            an + bn > N && break
            for c=primes
                cn = c^2
                n = an + bn + cn
                if n > N
                    break
                else
                    push!(res, n)
                end
            end
        end
    end
    ans = length(res)
    @info "P87: $ans"
    return ans
end  # function p87


@time p87(50)

@time p87(5 * 10^7)