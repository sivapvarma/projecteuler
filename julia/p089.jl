

struct RN
    val::Int
end


a = RN(10)

b = Int(a)

import Base: Int

Int(x::RN) = x.val

b = Int(a)


const NUMERAL_MAP = [
    (1000, "M")
    (900,  "CM")
    (500,  "D")
    (400,  "CD")
    (100,  "C")
    (90,   "XC")
    (50,   "L")
    (40,   "XL")
    (10,   "X")
    (9,    "IX")
    (5,    "V")
    (4,    "IV")
    (1,    "I")
]

function fromroman(str::AbstractString)
    # Strip whitespace and make uppercase
    str = uppercase(str)
    i = 1
    val = 0
    strlen = length(str)
    for (num_val, numeral) in NUMERAL_MAP
        numlen = length(numeral)
        while i+numlen-1 <= strlen && str[i:i+numlen-1] == numeral
            val += num_val
            i += numlen
        end
    end
    val
end

function toroman(val::Integer)
    val <= 0 && throw(DomainError(val, "in ancient Rome there were only strictly positive numbers"))
    val > 5000 && @warn("Roman numerals do not handle large numbers well")

    str = IOBuffer()
    for (num_val, numeral) in NUMERAL_MAP
        i = div(val, num_val)
        # Never concatenate an empty string to `str`
        i == 0 && continue
        print(str, repeat(numeral,i))
        val -= i*num_val
        # Stop when ready
        val == 0 && break
    end
    String(take!(str))
end

function p89()
    lines = readlines("../data/p089_roman.txt")
    res = 0
    for line in lines
        line = strip(line)
        r = toroman(fromroman(line))
        res += length(line) - length(r)
    end
    println("p89: $res")
    res
end  # function p89

# 743
@time p89()