import sys

tiles = []
max_area = 0
max_area_2 = 0

x_edges = {}
y_edges = {}

green_or_red = set()


with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.strip().split(",")
        tiles.append((int(line[0]), int(line[1])))


x_shrunk_to_exp = sorted([t[0] for t in tiles])
x_exp_to_shrunk = { val: i for i,val in enumerate(x_shrunk_to_exp)}
y_shrunk_to_exp = sorted([t[1] for t in tiles])
y_exp_to_shrunk = { val: i for i,val in enumerate(y_shrunk_to_exp)}


def in_edge(x, y):
    if x in x_edges:
        for low,high in x_edges[x]:
            if low <= y <= high:
                return True
            
    if y in y_edges:
        for low,high in y_edges[y]:
            if low <= x <= high:
                return True
            
    return False


def green_or_red_not_edge(x, y):
    return (x, y) in green_or_red and not in_edge(x, y)


def in_shape(x, y):
    if (x, y) in green_or_red:
        return True

    if in_edge(x, y):
        green_or_red.add((x, y))
        return True
    
    if green_or_red_not_edge(x+1, y) or \
      green_or_red_not_edge(x-1, y) or \
      green_or_red_not_edge(x, y+1) or \
      green_or_red_not_edge(x, y-1):
        return True
    
    edges_crossed = 0
    edge_just_crossed = False
    for x_next in range(x + 1, 1001):
        if not in_edge(x_next, y):
            edge_just_crossed = False
        elif not edge_just_crossed:
            edges_crossed += 1
            edge_just_crossed = True
        
    if edges_crossed % 2 == 0:
        return False
    
    green_or_red.add((x, y))
    return True


def valid_rect(x1, y1, x2, y2):
    x_low,x_high = sorted((x1, x2))
    y_low,y_high = sorted((y1, y2))

    for x in range(x_low, x_high+1):
        if not in_shape(x, y_low) or not in_shape(x, y_high):
            return False
        
    for y in range(y_low, y_high+1):
        if not in_shape(x_low, y) or not in_shape(x_high, y):
            return False
        
    center_x = (x_low + x_high) // 2
    center_y = (y_low + y_high) // 2

    return in_shape(center_x, center_y)


for i in range(len(tiles)):
    tile1 = tiles[i]
    tile2 = tiles[(i + 1) % len(tiles)]

    x1 = x_exp_to_shrunk[tile1[0]]
    x2 = x_exp_to_shrunk[tile2[0]]
    y1 = y_exp_to_shrunk[tile1[1]]
    y2 = y_exp_to_shrunk[tile2[1]]

    if x1 == x2:
        if x1 in x_edges:
            x_edges[x1].append(sorted((y1, y2)))
        else:
            x_edges[x1] = [sorted((y1, y2))]

    if y1 == y2:
        if y1 in y_edges:
            y_edges[y1].append(sorted((x1, x2)))
        else:
            y_edges[y1] = [sorted((x1, x2))]


for i,tile1 in enumerate(tiles):
    for j in range(i, len(tiles)):
        tile2 = tiles[j]

        area = (abs(tile1[0] - tile2[0]) + 1) * (abs(tile1[1] - tile2[1]) + 1)
        max_area = max(max_area, area)

        x1,y1 = (x_exp_to_shrunk[tile1[0]], y_exp_to_shrunk[tile1[1]])
        x2,y2 = (x_exp_to_shrunk[tile2[0]], y_exp_to_shrunk[tile2[1]])
        if valid_rect(x1, y1, x2, y2):
            max_area_2 = max(max_area_2, area)


print(f"Part 1: {max_area}")
print(f"Part 2: {max_area_2}")
