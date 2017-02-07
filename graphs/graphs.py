m = 4
n = 6
max = 6

node_str = '\\node (A{i}) at ({x}, {y}) [circle,draw] {{}};\n'
for i in range(m):
    x, y = 10 / (m -  1) * i, 0
    print(node_str.format(**locals()))

node_str = '\\node (B{i}) at ({x}, {y}) [circle,draw] {{}};\n'
for i in range(n):
    x, y = 10 / (n - 1) * i, 2
    print(node_str.format(**locals()))

edge_str = '\\draw (A{i}) to (B{j});\n'
for i in range(m):
    for j in range(n):
        print(edge_str.format(**locals()))


