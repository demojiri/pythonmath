import networkx as nx

with open('/usr/src/app/data/matrix.txt') as f:
    lines = f.read().splitlines()
f.close()

data = list(map(lambda line: list(map(lambda x: int(x), line.split(','))), lines))

g = nx.DiGraph()

for row_id, row in enumerate(data, start=0):
    for el_id, el in enumerate(row, start=0):
        g.add_node((row_id, el_id))
        if el_id > 0:
            g.add_edge((row_id, el_id-1), (row_id, el_id), weight=data[row_id][el_id])

        if row_id > 0:
            g.add_edge((row_id-1, el_id), (row_id, el_id), weight=data[row_id][el_id])


p = nx.dijkstra_path_length(g, source=(0, 0), target=(len(data)-1, len(data)-1))

print(p + data[0][0])
