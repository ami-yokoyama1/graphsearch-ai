import matplotlib.pyplot as plt
import networkx as nx
import random
import csv 
import pandas as pd
from collections import deque, defaultdict

"""
These are Function Headers
Complete the functions to ensure they return expected results
Replace these comments with documenation about the program
@author [add your name]
"""

def main():
        
    with open('./graph.csv', newline='') as csvfile:
        routes = pd.read_csv(csvfile, header= 0, usecols = ['Source', 'Dest', 'distance'])

    graph = nx.from_pandas_edgelist(routes, source = 'Source', target = 'Dest',
        edge_attr = 'distance', create_using = nx.DiGraph())
    
    # graph of the entire map:
    # plt.figure(figsize=(10, 9))
    # nx.draw_networkx(graph)
    # plt.savefig("dist_map.png", format="PNG", dpei = 300)
    # plt.show()

    # prints all edges sourced from Fremont:
    # print(list(nx.bfs_edges(graph, source = 'Fremont')))

    G = nx.balanced_tree(5,2, create_using=nx.DiGraph(incoming_graph_data=graph))
    source = 'Fremont'
    target = 'Ballard'
    bfs = mybfs(G, source, target)
    print(bfs)
    colors = ['red' if edge in bfs else 'blue' for edge in G.edges()]
    markers = ['green' if node in [source,target] else 'blue' for node in G.nodes()]
    nx.draw(G, edge_color = colors, node_color = markers, with_labels=True)
    plt.savefig("example_bfs.png") #or use plt.show() to display
    plt.show()

    # dfs = mydfs(G, source, target)
    # print(dfs)
    # colors = ['red' if edge in dfs else 'blue' for edge in G.edges()]
    # markers = ['green' if node in [source, target] else 'blue' for node in G.nodes()]
    # nx.draw(G, edge_color = colors, node_color = markers, with_labels=True)
    # plt.savefig("example_dfs.png") #or use plt.show() to display

def mybfs(G, source, target):
    """
    Return the searched edges as list of tuples
    """
    # if not G.has_key(source):
    #     raise AttributeError("The source '%s' is not in the graph" % source)
    # if not G.has_key(target):
    #     raise AttributeError("The target '%s' is not in the graph" % target)

    parents = {source: None}
    queue = deque([source])
    while queue:
        node = queue.popleft()
        for neighbor in G[node]:
            if neighbor not in parents:
                parents[neighbor] = node
                queue.append(neighbor)
                if neighbor == target:
                    break

    path = [target]
    while parents[target] is not None:
        path.insert(0, parents[target])
        target = parents[target]

    return path

def mydfs(G, source, target):
    """
    Return the searched edges as list of tuples
    """
    path = []

    queue = []
    queue.append(source)
    while queue:
        node = queue.pop()
        if node not in path:
            path.append(node)
            if node == target:
                break
            queue.extend(G[node])
    
    return path

def myastar(G, source, target):
    """
    Return the list of nodes in the path and total cost like ([1,2,3],9)
    """
    pass

### Do NOT remove the following lines of code
if __name__ == "__main__":
    main()