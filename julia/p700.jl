include("euler.jl")

P = big(4503599627370517)
K = big(1504170715041707)

is_prime(P)
is_prime(K)

g = gcdx(K, P)
Kinv = g[2]
if Kinv < 0
    Kinv = (Kinv + P) % P
end

function p700()
    ecoins = [(1, K)]
    min_ecoin = K
    n = big(1)
    while true
        n += 1
        res = K*n % P
        if res < min_ecoin
            println("n = $n, $res")
            push!(ecoins, (n,res))
            min_ecoin = res
        end
        res==15806432 && break
    end
    # println("n = $n, $min_ecoin")
    idx, ecoin = n, min_ecoin
    while ecoin > 1
        idx, ecoin = nextcoin(idx, ecoin-1)
        
        println("n = $idx, $ecoin")
        push!(ecoins, (idx, ecoin))
        
    end
    ecoins_d = Dict(ecoins)
    p700 = sum(values(ecoins_d))
    println("P700: $p700.") 
end  # function p700

function nextcoin(index, num)
    min_diff = P + 1
    N, coin = 0, 0
    while num > 0
        n = ( num * Kinv ) % P
        diff = abs(index - n)
        if diff < min_diff
            min_diff = diff
            N, coin = n, num
        end
        num -= 1
    end
    return N, coin
end  # function nextcoinindex, num

@time p700()
