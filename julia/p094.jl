function is_perfect_square(n::T) where {T<:Number}
    sn = isqrt(n)
    # return isapprox(rem(sn, 1), 0, atol=1e-10)
    return sn^2 == n
end  # function is_perfect_square


# based on heron's formula
function check_triangle(a::T, b::T, c::T) where {T<:Number}
    s = (a + b + c)/2
    # a2 = s*(s-a)*(s-b)*(s-c)
    a = (s-a)*sqrt(s*(s-c))
    return isapprox(rem(a, 1), 0, atol=1e-6)
    # a = div(a, 1)
    # return a2 == a^2
    # return a%1 == 0
    # return is_perfect_square(a2)
end # function check_triangle

"""
Area = (c/2) * sqrt( a*a - c*c/4 )
so for area to be integer:
    1. c has to be even
    2. a^2 - c^2/4 has to be a perfect square.
"""
function check(a::T, c::T) where {T<:Number}
    # s = a + (c/2)
    # a2 = (s-a)*sqrt(s*(s-c))
    cb2, r = divrem(c, 2)
    r != 0 && return false
    a2 = a^2 - cb2^2
    # @show a2
    return is_perfect_square(a2)
    # a = sqrt(a2)
    # af = floor(Int, a)
    # return isapprox(a, af, atol=1e-10)
end # function check
    

function p94(L::Int=10^9)
    @show L
    res = 0
    for a in 2:L
        p = 3*a + 1
        # if p <= L && check_triangle(a, a, a+1)
        if p <= L && check(a, a+1)
            # res += check(a, a+1)
            res += p
        end
        a < 2 && continue
        p = 3*a - 1
        p > L && break
        # if check_triangle(a, a, a-1)
        if check(a, a-1)
            res += p
        end
        # res += check(a, a-1)
    end
    println("p94: $res")
    res
end  # function p94

@time p94(100)

# p94: 518408346
#   6.318927 seconds (71 allocations: 3.656 KiB)
@time p94()

check_triangle(5, 5, 6)