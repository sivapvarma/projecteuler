using Random
using Printf


squares = [
  "GO",  "A1", "CC1",  "A2",  "T1",  "R1",  "B1", "CH1",  "B2",  "B3",
"JAIL",  "C1",  "U1",  "C2",  "C3",  "R2",  "D1", "CC2",  "D2",  "D3",
  "FP",  "E1", "CH2",  "E2",  "E3",  "R3",  "F1",  "F2",  "U2",  "F3",
 "G2J",  "G1",  "G2", "CC3",  "G3",  "R4", "CH3",  "H1",  "T2",  "H2"
]


NUM_SQUARES = length(squares)
NUM_DIE_SIDES = 4

die() = rand(1:NUM_DIE_SIDES)
dice() = die(), die()

square_idx = Dict( (v, k-1) for (k, v) in enumerate(squares))

idx_square = Dict( (v, k) for (k, v) in square_idx )

# function iscallable(f)
#     try
#         f("GO")
#         return true
#     catch MethodError
#         return false
#     end
# end

iscallable(f) = !isempty(methods(f))

ident(x) = x

next_idx(i) = (i + 1) % NUM_SQUARES

next_idx(0)

function nextR(cs::String)
    idx = square_idx[cs]
    idx = next_idx(idx)
    while idx_square[idx][1] != 'R'
        idx = next_idx(idx)
        # @info "idx = $idx, $(idx_square[idx])"
    end
    return idx_square[idx]
end  # function nextR

function nextU(cs::String)
    idx = square_idx[cs]
    idx = next_idx(idx)
    while idx_square[idx][1] != 'U'
        idx = next_idx(idx)
        # @info "idx = $idx, $(idx_square[idx])"
    end
    return idx_square[idx]
end # function nexTU


function back3(cs::String)
    idx = square_idx[cs]
    idx = (idx + NUM_SQUARES - 3) % NUM_SQUARES
    return idx_square[idx]
end # function back3

nextR("A2")
nextR("JAIL")

nextU("JAIL")
nextU("U1")


CC_cards = [ident, ident, ident, ident,
            ident, ident, ident, ident,
            ident, ident, ident, ident,
            ident, ident,
            "GO",
            "JAIL"]


CH_cards = [ident, ident, ident, ident,
            ident, ident,
            "GO",
            "JAIL",
            "C1",
            "E3",
            "H2",
            "R1",
            nextR,
            nextR,
            nextU,
            back3]


function p84(num_turns::Int=1000000)
    freq = Dict( (sq, 0) for sq in squares )

    decks = Dict(
        "CC" => shuffle(CC_cards),
        "CH" => shuffle(CH_cards)
    )

    cs = "GO"

    freq[cs] += 1

    for t in 1:num_turns

        cont_rolling = true
        doubles = 0
        while cont_rolling
            d1, d2 = dice()
            cont_rolling = d1 == d2

            if cont_rolling
                doubles += 1
                if doubles == 3
                    cs = "JAIL"
                    frequencies[cs] += 1
                    break
                end
                continue
            end

            idx = square_idx[cs]
            idx = (idx + d1 + d2) % NUM_SQUARES
            cs = idx_square[idx]
        
            # handle special cards

            cc_or_ch = cs[1:2] in ["CC", "CH"]

            if cs == "G2J"
                cs = "JAIL"
            elseif cc_or_ch
                deck = decks[cs[1:2]]
                card = deck[1]
                decks[cs[1:2]] = deck[[2:end; 1]]

                if iscallable(card)
                    cs = card(cs)
                else
                    cs = card
                end
            end

            if !cont_rolling
                freq[cs] += 1
            end
        end
    end

    order = sort(collect(freq), by=x->x[2], rev=true)
    order = map(x->x[1], order)
    @show order[1:3]
    res = join([@sprintf "%02d" square_idx[s] for s = order[1:3]])
    println("p084; $res")
    return res
end

# 101524
@time p84()



