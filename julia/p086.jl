function shortest_path(cuboid)
    l, b, h = cuboid
    a = [l, b, h]
    sort!(a, rev=true)    

    
end  # function shortest_pathcuboid


function is_perfect_square(n::Int)
    n < 0 && return false
    sn = sqrt(n)
    isn = floor(Int, sn)
    return isn == sn
end  # function is_perfect_square

function check_int_sp(l::Int, b::Int, h::Int)
    d2 = l^2 + (b + h)^2
    return is_perfect_square(d2)
end  # function check_int_sp

function ncuboids(M::Int)
    num = 0
    l = M
    for b=1:l
        for h=1:b
            if check_int_sp(l, b, h)
                num += 1
            end
        end
    end
    return num
end  # function ncuboids

function p86()
sols = 0
m = 0
while true
    m += 1
    sols += ncuboids(m)
    println("$m: $sols")
    sols > 1000_000 && break
end
println("p86: $m")
end  # function p86

@time p86()