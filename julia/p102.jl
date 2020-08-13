using CSV


struct Point{T<:Number}
    x::T
    y::T
end

struct Triangle{T<:Number}
    A::Point{T}
    B::Point{T}
    C::Point{T}
end

function Triangle(x1::T, y1::T, x2::T, y2::T, x3::T, y3::T) where {T<:Number}
    a = Point(x1, y1)
    b = Point(x2, y2)
    c = Point(x3, y3)
    return Triangle(a, b, c)
end

struct Line{T<:Number}
    a::T
    b::T
    c::T
end

function (l::Line)(p::Point)
    return l.a * p.x + l.b * p.y + l.c
end  # function (l::Line)


# return true if origin falls inside the triangle.
function test_traingle(t::Triangle)::Bool
    ts = [false, false, false]
    ts[1] = test_line_point(t.A, t.B, t.C)
    ts[2] = test_line_point(t.B, t.C, t.A)
    ts[3] = test_line_point(t.C, t.A, t.B)
    return all(ts)
end  # function test_traingle

# Test if C and Origin fall on the same side of line A--B.
function test_line_point(A::Point, B::Point, C::Point)
    l = line_equation(A, B)
    origin = Point(0, 0)
    m = l(origin)
    n = l(C)
    return m*n >= 0
end  # function test_line_point

function line_equation(A::Point, B::Point)
    a, b, c = 0.0, 0.0, 0.0
    if A.x == B.x
        a = 1.0
        b = 0.0
        c = float(A.x)
    else
        b = -1.0
        a = (B.y - A.y)/(B.x - A.x)
        c = A.y - a * A.x
    end
    return Line(a, b, c)
end # function line_equation


p1 = Point(-340, 495)
p2 = Point(-153, -910)
p3 = Point(835, -947)

t1 = Triangle(p1, p2, p3)

test_traingle(t1)

t2 = Triangle(-175,41,421,-714,574,-645)

test_traingle(t2)

function p102()
    cnt = 0
    for row in CSV.File("../data/p102_triangles.txt"; header=["x1", "y1", "x2", "y2", "x3", "y3"], type=Int)
        # println(row.x1, row.x2)
        t = Triangle(row.x1, row.y1, row.x2, row.y2, row.x3, row.y3)
        cnt += test_traingle(t)
    end
    println("p102: $cnt")
end  # function p102

@time p102()



