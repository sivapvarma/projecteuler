using StrLiterals, StrFormat

s = "euler99.py"

if occursin(r"\d+", s)
    m = match(r"\d+", s)
    println(f"p\{0>3}(m.match).py")
end

function renamefiles()
    cd("/Users/sivapvarma/Github/projecteuler/python")
    pwd()
    for fn in readdir()
        if occursin(r"\d+", fn)
            m = match(r"\d+", fn)
            nfn = f"p\{0>3}(m.match).py"
            println(fn, " => ", nfn)
            mv(fn, nfn)
        end
    end
end  # function renamefiles


# 0.021215 seconds (1.68 k allocations: 90.766 KiB)
@time renamefiles()