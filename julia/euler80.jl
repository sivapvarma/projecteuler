function square_root_digits(n, iter=1000)
    # currently assumes that n < 100
    a, b = big(5*n), big(5)
    for i in 1:iter
        if a >= b
            a, b = a-b, b+10
        else
            a, b = a*100, 10*b - 45
        end
    end
    return b
end

r = 0

for i =1:99
    s = 0
    sq_rt = square_root_digits(i, 1000)
    d = digits(sq_rt, 10)
    for idx = 0:99
        s += d[end-idx]
    end
    println("$i\t>>>\t$s")
    r += s
end
println("PE80 Ans: $(r-45)")
