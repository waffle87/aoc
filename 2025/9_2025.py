import shapely

input = open("data/9_2025.txt")
data = input.read().splitlines()
p = []

for i in data:
    x, y = [int(x) for x in i.split(",")]
    p.append((x, y))

polygon = shapely.Polygon(p)
shapely.prepare(polygon)
p1, p2 = 0, 0

for i in p:
    for j in p:
        corners = [i, (i[0], j[1]), j, (j[0], i[1])]
        area = abs(i[0] - j[0] + 1) * abs(i[1] - j[1] + 1)
        if area > p1:
            p1 = area
        rect = shapely.Polygon(corners)
        if polygon.contains(rect) and area > p2:
            p2 = area

print(p1)
print(p2)
