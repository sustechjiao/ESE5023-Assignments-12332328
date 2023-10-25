#test3

def generate_pascals_triangle_line(k):
    line = [1]
    for i in range(1, k + 1):
        next_val = line[-1] * (k - i + 1) // i
        line.append(next_val)
    return line

def Pascal_triangle(k):
    triangle = []
    for i in range(k):
        triangle.append(generate_pascals_triangle_line(i))
    return triangle

line_100 = Pascal_triangle(100)
print(" (Line 100):", line_100[-1])

line_200 = Pascal_triangle(200)
print(" (Line 200):", line_200[-1])
