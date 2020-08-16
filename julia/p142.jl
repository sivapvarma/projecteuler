using Combinatorics

a = [25, 16, 9]

function pyth_triplet_seq(limit::Int=100)
    slimit = floor(Int, sqrt(limit))
    Channel() do ch
        for sz in 1:slimit
            for sy in sz+1:slimit
                y = sy^2
                z = sz^2
                x = y + z
                is_perfect_square(x) && put!(ch, (x, y, z))
            end
        end
    end
end


trips = pyth_triplet_seq(1000000000000)
for t in trips
    if check_squares(t)
        println("$t, $(check_squares(t))")
    end
end

function is_perfect_square(n::Int)
    n < 0 && return false
    sn = sqrt(n)
    sn_i = floor(Int, sn)
    return sn_i == sn
end

function check_squares(t)
    x, y, z = t
    for (a,b) in combinations(t, 2)
        !is_perfect_square(abs(a-b)) && return false
        !is_perfect_square(abs(a+b)) && return false
    end
    return true
end  # function check_squarets


limit = 100000

for z in 1:limit
    for y in (z+1):limit
        y2, z2 = y^2, z^2
        if is_perfect_square(y2 + z2) && is_perfect_square(y2 - z2)
            println("$y2, $z2")
        end
    end
end


function p142(limit = 10000)
    slimit = floor(Int, sqrt(limit))
    for ai = 1:slimit
        a = ai^2
        for ei = 1:(ai-1)
            e = ei^2
            for ci = 1:(ei-1)
                c = ci^2
                b = e - c
                d = a - e
                f = a - c
                b <= 0 && continue
                d <= 0 && continue
                f <= 0 && continue
                !is_perfect_square(b) && continue
                !is_perfect_square(d) && continue
                !is_perfect_square(f) && continue
                x, y, z = (a+b), (c+d), (e-f)
                x%2 != 0 && continue
                y%2 != 0 && continue
                z%2 != 0 && continue
                x, y, z = x/2, y/2, z/2
                x <= 0 && continue
                y <= 0 && continue
                z <= 0 && continue

                println("$x, $y, $z, $(round(Int, x+y+z))")
                println("$a, $b, $c, $d, $e, $f")
                return x + y + z
            end
        end
    end
end  # function p142

@time p142(1000000)