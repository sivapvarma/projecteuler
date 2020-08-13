A = readcsv("../data/p081_matrix.txt")
h, w = size(A)
B = zeros(A)
for i in 1:h
    for j in 1:w
        if i==1 && j==1
            B[i, j] = A[i, j]
        elseif i==1
            B[i,j] = A[i,j] + B[i,j-1]
        elseif j==1
            B[i,j] = A[i,j] + B[i-1,j]
        else
            B[i,j] = A[i,j] + min( B[i,j-1], B[i-1,j] )
        end
    end
end
println("PE81 Ans: $(B[h,w])")
