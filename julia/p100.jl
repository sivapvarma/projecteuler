function check_brute_force(m, n)
    prob = (m*(m-1)) / ((m+n)*(m+n-1))
    if prob == 1/2
        return true
    else
        return false
    end
end

function check_1(m, n)
    lv = (m+n-1)*(m-n)
    rv = m*2*n
    if lv == rv
        return true
    else
        return false
    end
end

function checker(limit, check)
    for m=1:limit
        for n=1:round(m/2)
            if check(m, n)
                println("$m, $n, sum = $(m+n)")
            end
        end
    end
end

# limit = 100000
limit = 10^12

# println("Using Brute force")
# @time checker(limit, check_brute_force)
# 
# println("Using Optimized version")
# @time checker(limit, check_1)

# Dario Alpern's Generic two integer quadratic Diophantine Equation solver
# http://www.alpertron.com.ar/QUAD.HTM
# Try to port his java solver to Julia or Python or Javascript.It is a mess
# methods: http://www.alpertron.com.ar/METHODS.HTM
b, n = 1, 1
println("$b, $n")
while n < limit
    b, n = 3b+2n-2, 4b+3n-3
    println("$b, $n")
end

# these give negative values ??
# println("Different Initial Conditions")
# b, n = 0, 1
# println("$b, $n")
# while n < limit
#     b, n = 3b+2n-2, 4b+3n-3
#     println("$b, $n")
# end
