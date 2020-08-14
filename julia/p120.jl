function AN(a::Int)
    function an(n::Int)
        return ( (a-1)^n + (a+1)^n ) % a^2
    end  # function ann::Int
    return an
end  # function AN

function p120_test()
    a = 7
    a2 = a^2
    # rmax = -Inf
    for n=1:a^2
        r = ( powermod(a-1, n, a2) + powermod(a+1, n, a2) ) % (a2)
        println("$a, $n, $r")
        # if rmax < r
        #     println("$a, $n, $r")
        #     rmax = r
        # end 
    end
end  # function p120

@time p120_test()

function p120()
    res = 0
    for a=3:1000
        res += 2*a*floor(Int, (a-1)/2)
    end
    println("p120: $res")
end  # function p120

@time p120()