import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('edge_list.csv')
print(df)
gr = nx.Graph()

# iterate through the column "locations" and add each as a node
# iterate through origin and destination, add each respective point as an edge. Label them according to the "route" column


node_graph = nx.from_pandas_edgelist(df, source='Source', target='Target', edge_key='Route',
                                     edge_attr=True,
                                     create_using=nx.MultiDiGraph)
node_graph = node_graph.to_undirected()

gpos = nx.shell_layout(node_graph)  # make a variable containing not positions
nx.draw_networkx(node_graph, node_size= 750, pos=gpos, font_size=5)  # draw the graph
nx.draw_networkx_nodes(node_graph, pos=gpos)
nx.draw_networkx_edges(node_graph, pos=gpos, node_size=500)
nx.draw_networkx_edge_labels(node_graph, pos=gpos, font_size=8,
                                 edge_labels={(u, v): w for u, v, w in node_graph.edges(data='Route')})  # add edge labels
plt.savefig('TCAT System Shell Layout', dpi=500)
plt.figure(figsize=(10, 10),dpi=100)
plt.draw()

plt.show()


