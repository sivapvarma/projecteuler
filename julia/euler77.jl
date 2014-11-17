function primes(n)
    p = [2, 3, 5, 7]
    for k in 11:n
        flag = true
        for r in p
            if k%r == 0
                flag = false
                break
            elseif r > sqrt(k)
                break
            end
        end
        if flag
            p = [p, k]
        end
    end
    p
end


function no_of_sum(n)
    global p
    println("primes array $p")
    l = length(p)
    r = 0
    for k in 1:l
        if p[k] >= n
            break
        else
            r += no_of_sums(n-p[k], k)
        end
    end
    r # return value
end

function no_of_sums(n, i)
    global p
    if i == 0 && n > 0
        return 0
    elseif n < p[i]
        return no_of_sums(n, i-1)
    elseif n == 0 && i > 0
        return 1
    else
        return no_of_sums(n-p[i], i) + no_of_sums(n, i-1)
    end
end

n = 60
println("primes below $n: $(primes(n))")
n = 100
global p
p = primes(100)
println("primes below $n: $(p)")
k = 5
println("No of ways of $k: $(no_of_sum(k))")

L, target = 5000, 11
while true
    ways = [1, zeros(target)]
    for prime in p
        
    end
end
