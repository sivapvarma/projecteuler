A = readcsv("../data/p082_matrix.txt")
R, C = size(A)
# Idea from http://stackoverflow.com/a/15558407/1034279
B = zeros(A)
for c in 1:C
    for r in 1:R
        if c==1
            B[r, c] = A[r, c]
        else
            B[r, c] = B[r, c-1] + A[r, c]
            for pr in 1:R
                tmp = B[pr, c-1] + (pr < r ? sum(A[pr:r, c]) : sum(A[r:pr,c]))
                B[r,c] = min(B[r,c], tmp)
            end
        end
    end
end

res = B[1, C]
for r in 1:R
    if res > B[r, C]
        res = B[r,C]
    end
end
println("PE82 Ans: $res")
