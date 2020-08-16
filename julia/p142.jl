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


function p142()
    limit = 10000
    slimit = floor(Int, sqrt(limit))
    for ai = 1:slimit
        a = ai^2
        for bi = 1:ai
            b = bi^2
            x = floor(Int, (a+b)/2)
            y = x - b
            for ci = 1:ai
                c = ci^2
                z = c + b - x
                d = y - z
                e = x + z
                f = x - z
                is_perfect_square(d) && continue
                is_perfect_square(e) && continue
                is_perfect_square(f) && continue
                println("$x, $y, $z, $(x+y+z)")
                return x + y + z
            end
        end
    end
end  # function p142

@time p142()