function is_palindrome(n::Int)
    nr = parse(Int, reverse(string(n)))
    return nr==n
end  # function is_palindrome

n = 0
for k=1:1000
    global n
    if is_palindrome(k)
        n += 1
        println("$n: $k")
    end
end

function p125(limit=10^8)
    sqlimit = round(Int, sqrt(limit))
    res = Set{Int}()
    for i=1:sqlimit
        n = i^2
        for j=i+1:sqlimit
            n += j^2
            n > limit && break
            if is_palindrome(n)
                push!(res, n)
            end
        end
    end
    sum_res = sum(res)
    num = length(res)
    @show res
    println("$num palindromes below $limit adding up to $sum_res")
end  # function p125

@time p125(1000)

@time p125()