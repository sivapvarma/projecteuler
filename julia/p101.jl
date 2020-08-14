using Polynomials
using Printf
#=
using Latexify
u = Polynomial([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1])

n = 2
function const_matrix(n::Int=2)

    
end  # function const_matrix

a = collect(1:n)

b = hcat([a.^k for k=0:n-1]...)

c = u.(a)

d = b \ c

u1 = Polynomial(d)

=#
function p101()
    u = Polynomial([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1])
    res = 1
    for n=2:10
        a = collect(1:n)
        A = hcat([a.^k for k=0:n-1]...) 
        b = u.(a)
        coefs = A \ b
        un = Polynomial(coefs)
        @show un
        res += un(n+1)
    end
    println(@sprintf "p101: %13.f" res)
end  # function p101

function p101_test()
    u = Polynomial([0, 0, 0, 1])
    res = 1
    for n=2:3
        a = collect(1:n)
        A = hcat([a.^k for k=0:n-1]...) 
        b = u.(a)
        coefs = A \ b
        un = Polynomial(coefs)
        @show un
        res += un(n+1)
    end
    println("p101 test: $res")
end  # function p101

@time p101_test()

@time p101()


# there is some interesting theory related to finite differences
# see difference engine on wikipedia.