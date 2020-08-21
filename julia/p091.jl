function is_right_tri(sides::Vector{T}) where {T<:Number}
    a, b, c = sort(sides)
    return c == a + b
end # function is_right_tri

function check(x1::Int, y1::Int, x2::Int, y2::Int)
    x1==0 && y1==0 && return false
    x2==0 && y2==0 && return false
    x1==x2 && y1==y2 && return false
    a = x1^2 + y1^2
    b = (x1-x2)^2 + (y1-y2)^2
    c = x2^2 + y2^2
    # return is_right_tri([a, b, c])
    return a+b+c == 2*max(a, b ,c)
end  # function checkx1::Int, y1::Int, x2::Int, y2::Int

function p91(L::Int=50)
    # res = 0
    res = Set{Set{Tuple{Int, Int}}}()
    for x1 in 0:L
        for y1 in 0:L
            for x2 in 0:L
                for y2 in 0:y1
                    if check(x1, y1, x2, y2)
                        # println("$x1, $y1, $x2, $y2")
                        # res += 1
                        push!(res, Set([(x1, y1), (x2, y2)]))
                    end
                end
            end
        end
    end
    r = length(res)
    println("p91: $r")
    r
end  # function p91

@time p91(2)

@time p91()