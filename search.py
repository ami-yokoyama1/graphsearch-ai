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
        routes = pd.read_csv(csvfile)
    
    graph = nx.from_pandas_edgelist(routes, source = 'Source', target = 'Dest',
        edge_attr = 'distance', create_using = nx.DiGraph())
    
    plt.figure(figsize=(10, 9))
    nx.draw_networkx(graph)
    plt.savefig("dist_map.png", format="PNG", dpi = 300)
    plt.show()

    G = nx.balanced_tree(5,2)
    source = 0
    target = 9
    bfs = mybfs(G, source, target)
    print(bfs)
    colors = ['red' if edge in bfs else 'blue' for edge in G.edges()]
    markers = ['green' if node in [source,target] else 'blue' for node in G.nodes()]
    nx.draw(G, edge_color = colors, node_color = markers, with_labels=True)
    plt.savefig("example_bfs.png") #or use plt.show() to display

    dfs = mydfs(G, source, target)
    print(dfs)
    colors = ['red' if edge in dfs else 'blue' for edge in G.edges()]
    markers = ['green' if node in [source, target] else 'blue' for node in G.nodes()]
    nx.draw(G, edge_color = colors, node_color = markers, with_labels=True)
    plt.savefig("example_dfs.png") #or use plt.show() to display

def mybfs(G, source, target):
    """
    Return the searched edges as list of tuples
    """
    q = deque()

    target[source] = True
    q.append(source)

    while q:
        currNode = q.popleft()
        print(currNode, end=" ")

        for n in G[currNode]:
            if not target[n]:
                target[n] = True
                q.append(n)

# def __init__(self):
#     self.graph = defaultdict(list)

# visited vs. target - aren't they different things?
def DFSUtil(G, source, target):
    """
    Return the searched edges as list of tuples
    """

    target.add(source)
    print(source, end= ' ')

    for n in G.graph[source]:
        if n not in target:
            G.DFSUtil(n, target)

def mydfs(G, source, target):
    target = set()
    G.DFSUtil(source, target)

def myastar(G, source, target):
    """
    Return the list of nodes in the path and total cost like ([1,2,3],9)
    """
    pass

### Do NOT remove the following lines of code
if __name__ == "__main__":
    main()