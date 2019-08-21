import math

class Point:
    def __init__(self):
        self.x = None
        self.y = None

def koch(d, p1, p2):
    if d == 0:
        return

    s = Point()
    u = Point()
    t = Point()
    rad = math.radians(60)

    s.x = (2 * p1.x + 1 * p2.x) / 3
    s.y = (2 * p1.y + 1 * p2.y) / 3
    t.x = (1 * p1.x + 2 * p2.x) / 3
    t.y = (1 * p1.y + 2 * p2.y) / 3
    u.x = (t.x - s.x) * math.cos(rad) - (t.y - s.y) * math.sin(rad) + s.x
    u.y = (t.x - s.x) * math.sin(rad) + (t.y - s.y) * math.cos(rad) + s.y
    
    koch(d-1, p1, s)
    print(s.x, s.y)
    koch(d-1, s, u)
    print(u.x, u.y)
    koch(d-1, u, t)
    print(t.x, t.y)
    koch(d-1, t, p2)

def main():
    n = int(input())
    a = Point()
    b = Point()

    a.x = 0.0
    a.y = 0.0
    b.x = 100.0
    b.y = 0.0

    print(a.x, a.y)
    koch(n, a, b)
    print(b.x, b.y)
    
             
if __name__ == "__main__":
    main()