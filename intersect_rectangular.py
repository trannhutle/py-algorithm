import collections

Rectangular = collections.namedtuple(
    "Rectangular", ("x", "y", "width", "height"))


def intersect_rectangular(R1, R2):
    def is_intersect(_R1, _R2):
        return (_R1.x <= _R2.x + _R2.width and _R1.x + _R1.width >= _R2.x and R1.y <= _R2.y + _R2.height and _R1.y + _R1.height >= _R2.y)

    print("is intersect", is_intersect(R1, R2))
    if not is_intersect(R1, R2):
        return Rectangular(0, 0, -1, -1)

    return Rectangular(
        max(R1.x, R2.x),
        max(R1.y, R2.y),
        min(R1.x + R1.width, R2.x + R2.width) - max(R1.x, R2.x),
        min(R1.y + R1.height, R2.y + R2.height) - max(R1.y, R2.y)
    )


r1 = Rectangular(x=1, y=1, width=15, height=15)
r2 = Rectangular(x=3, y=5, width=20, height=20)

print(intersect_rectangular(r1, r2))
