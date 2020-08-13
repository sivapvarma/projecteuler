function fibonacci_seq()
    # generator of fibonacci numbers
    a, b = zero(BigInt), one(BigInt)
    Channel() do ch
        while true
            put!(ch, b)
            a, b = b, a + b
        end
    end
end  # function fibonacci

function is_pandigit(s::String)
    digits = [false for i=1:9]
    for d in s
        d = parse(Int, d)
        d == 0 && break
        digits[d] = !digits[d]
    end
    return all(digits)
end  # function is_pandigit

function is_pan19(s::String)::Bool
    ds = Set(s)
    return '0' ∉ ds && length(ds) == 9
end  # function is_pan19

function check104(n::T) where {T<:Union{Int, BigInt}}
    ns = string(n)
    return length(ns) >= 9 && is_pandigit(ns[begin:begin+8]) && is_pandigit(ns[end-8:end])
end  # function check104

function check104_set(n::T) where {T<:Union{Int, BigInt}}
    ns = string(n)
    return length(ns) >= 9 && is_pan19(ns[begin:begin+8]) && is_pan19(ns[end-8:end])
end  # function check104_set

function check_last(n::T) where {T<:Union{Int, BigInt}}
    ns = string(n)
    return length(ns) >= 9 && is_pandigit(ns[end-8:end])
end  # function check_last

function check_first(n::T) where {T<:Union{Int, BigInt}}
    ns = string(n)
    return length(ns) >= 9 && is_pandigit(ns[begin:begin+8])
end  # function check_first

F = fibonacci_seq()
for (i, v) in enumerate(F)
    # println("F$i = $v")
    if check_first(v)
        println("Fibonacci $i and it has $(length(string(v))) digits.")
        break
    end
end

F = fibonacci_seq()
for (i, v) in enumerate(F)
    # println("F$i = $v")
    if check_last(v)
        println("Fibonacci $i and it has $(length(string(v))) digits.")
        break
    end
end

function p104()
    F = fibonacci_seq()
    for (i, v) in enumerate(F)
        # println("F$i = $v")
        if check104(v)
            println("Fibonacci $i and it has $(length(string(v))) digits.")
            break
        end
    end
end  # function p104

function p104_set()
    F = fibonacci_seq()
    for (i, v) in enumerate(F)
        # println("F$i = $v")
        if check104_set(v)
            println("Fibonacci $i and it has $(length(string(v))) digits.")
            break
        end
    end
end  # function p104_set

# Ans: 329468
@time p104()

@time p104_set()

function fibonacci(n::Int)::BigInt
    f_n_1, f_n_2 = big(1), big(1)
    n <= 0 && return 0
    n == 1 && return 1
    n == 2 && return 1
    for k=3:n
        f = f_n_1 + f_n_2
        f_n_2 = f_n_1
        f_n_1 = f
    end
    return f_n_1
end  # function fibonaccin::Int

for n=1:20
    println("$n \t $(fibonacci(n))")
end

@time n = fibonacci(329468);println(length(string(n)));


res = 329468

A = Set(string(res))




sq5 = sqrt(big(5.0))
root = (1 + sq5)/2

function fiba(n::Int)::BigFloat
    return root^n/sq5
end

n = fiba(329468)

function num_of_digits_fib(n::Int)::Int
    fn = fiba(n)
    fns = string(fn)
    if '+' in fns
        fns_sp = split(fns, '+')
        nd = parse(Int, fns_sp[2]) + 1 
    else
        fns_sp = split(fns, '.')
        nd = length(fns_sp[1])
    end
    return nd
end  # function num_of_digits_fibn::Int

# assume n is sufficiently larger
function fib_first9(n::Int)
    fn = fiba(n)
    fns = string(fn)
    fns = replace(fns, "."=>"")
    return parse(Int, fns[begin:begin+8])
end  # function fib_first9n::Int::Int

function fibonacci_last9_seq()
    # generator of fibonacci numbers
    a, b = 0, 1
    Channel() do ch
        while true
            put!(ch, b)
            a, b = b, a + b
            if b > 10^9
                b = b % 10^9
            end
        end
    end
end  # function fibonacci_last9_seq

fiblast9 = fibonacci_last9_seq()
for (i, v) in enumerate(fiblast9)
    fn = fibonacci(i)
    println("$i: $(fn%10^9) $v")
    i==100 && break
end

function p104_fast()
    fiblast9 = fibonacci_last9_seq()
    for (k, v) in enumerate(fiblast9)
        !is_pan19(string(v)) && continue
        f9 = fib_first9(k)
        if is_pan19(string(f9))
            println("Fibonacci $k and it has $(num_of_digits_fib(k)) digits.")
            break
        end
    end
end  # function p104_fast

# 10.945169 seconds (5.60 M allocations: 226.865 MiB, 0.18% gc time)
@time p104_fast()

# @profview p104_fast()

for n=1:200
    fn = fibonacci(n)
    fns = string(fn)
    fns_nd = length(fns)
    nd = num_of_digits_fib(n)
    println("$n \t $fn \t $fns_nd \t $nd")
end