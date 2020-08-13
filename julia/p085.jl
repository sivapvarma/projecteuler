function C2(n)
    return div(int(n*(n-1)), 2)
end

# for i in 40:60
#     println("$i C 2 = $(C2(i))")
# end

val = 2000000
diff = val
r, c, vf = 1, 1, val
for row in 1:100
    for col in 1:100
        v = C2(row+1)*C2(col+1)
        tmp = abs(v-val)
        if tmp < diff
            diff = tmp
            r, c, vf = row, col, v
        end
    end
end
println("PE85 Ans: $r x $c = $(r*c) >>> No of rectangles: $vf")
