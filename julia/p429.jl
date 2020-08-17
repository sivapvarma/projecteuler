using Combinatorics

include("euler.jl")

is_prime(10^9 + 9)

P = 10^9 + 9

@time primes = eratosthenes(P)

length(primes)


function prime_exp(n::Int, p::Int)
    res = 0
    k = p
    while n >= k
        res += floor(Int, n/k)
        k *= p
    end
    return res
end  # function prime_exp

N = 4
primes = eratosthenes(N)
for p in primes
    pe = prime_exp(N, p)
    @show p pe
end

function p429(N::Int)
    @info "N = $N"
    P = 10^9 + 9
    @time primes = eratosthenes(min(P, N))
    prime_divisors = Int[]
    # 1 is not included in this list
    for p in primes
        p > N && break
        pe = prime_exp(N, p)
        push!(prime_divisors, powermod(p, pe, P))
    end
    @info "Done computing pure prime divisors"
    no_prime_divisors = length(prime_divisors)
    @info "$no_prime_divisors prime divisors."
    res =  1
    for pd in prime_divisors
        res = (res * (1 + powermod(pd, 2, P))) % P
    end
    # for k = 1:no_prime_divisors
    #     @info "k = $k"
    #     for dt in combinations(prime_divisors, k)
    #         unitary_divisor = reduce(*, dt)
    #         res = ( res + powermod(unitary_divisor, 2, P) ) % P
    #     end
    # end
    return res
end  # function p429

@time p429(4)

@time p429(100)

@time p429(1000)

@time p429(10^8)