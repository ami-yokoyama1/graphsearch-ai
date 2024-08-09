import matplotlib.pyplot as plt
import networkx as nx
import random
from itertools import count
import csv 
import pandas as pd
from collections import deque, defaultdict
import heapq
from heapq import heappop, heappush
from networkx.algorithms.shortest_paths.weighted import _weight_function
import math


"""
These are Function Headers
Complete the functions to ensure they return expected results
Replace these comments with documenation about the program
@author [Ami Yokoyama]
"""

def main():
        
    with open('./graph.csv', newline='') as csvfile:
        routes = pd.read_csv(csvfile, header= 0, usecols = ['Source', 'Dest', 'distance'])

    graph = nx.from_pandas_edgelist(routes, source = 'Source', target = 'Dest',
        edge_attr = 'distance', create_using = nx.Graph())
    
    # graph of the entire map:
    # plt.figure(figsize=(10, 9))
    # nx.draw_networkx(graph)
    # plt.savefig("dist_map.png", format="PNG", dpei = 300)
    # plt.show()

    # prints all edges sourced from Fremont:
    # print(list(nx.bfs_edges(graph, source = 'Fremont')))

    # driver code for bfs:
    source = 'Ballard'
    target = 'Columbia City'
    bfs = mybfs(graph, source, target)
    print(bfs)
    colors = ['red' if edge in bfs else 'blue' for edge in graph.edges()]
    markers = ['green' if node in [source,target] else 'blue' for node in graph.nodes()]
    fig, axe = plt.subplots(figsize=(12, 7))
    axe.set_title(f"BFS: Total cost of the final path: {len(bfs)-1}", loc='right')
    nx.draw(graph, ax = axe, edge_color = colors, node_color = markers, with_labels=True)
    plt.savefig("example_bfs.png")
    # plt.show()

    source = 'West Seattle'
    target = 'Magnolia'
    bfs = mybfs(graph, source, target)
    print(bfs)
    colors = ['red' if edge in bfs else 'blue' for edge in graph.edges()]
    markers = ['green' if node in [source,target] else 'blue' for node in graph.nodes()]
    fig, axe = plt.subplots(figsize=(12, 7))
    axe.set_title(f"BFS: Total cost of the final path: {len(bfs)-1}", loc='right')
    nx.draw(graph, ax = axe, edge_color = colors, node_color = markers, with_labels=True)
    plt.savefig("bfs.wm.png")

    # driver code for dfs:
    source = 'Ballard'
    target = 'Columbia City'
    dfs = mydfs(graph, source, target)
    print(dfs)
    colors = ['red' if edge in dfs else 'blue' for edge in graph.edges()]
    markers = ['green' if node in [source, target] else 'blue' for node in graph.nodes()]
    fig, axe = plt.subplots(figsize=(12, 7))
    axe.set_title(f"DFS: Total cost of the final path: {len(dfs)-1}", loc='right')
    nx.draw(graph, ax = axe, edge_color = colors, node_color = markers, with_labels=True)
    plt.savefig("example_dfs.png")
    # plt.show()

    source = 'West Seattle'
    target = 'Magnolia'
    dfs = mydfs(graph, source, target)
    print(dfs)
    colors = ['red' if edge in dfs else 'blue' for edge in graph.edges()]
    markers = ['green' if node in [source, target] else 'blue' for node in graph.nodes()]
    fig, axe = plt.subplots(figsize=(12, 7))
    axe.set_title(f"DFS: Total cost of the final path: {len(dfs)-1}", loc='right')
    nx.draw(graph, ax = axe, edge_color = colors, node_color = markers, with_labels=True)
    plt.savefig("dfs.wm.png")

    # driver code for astar:
    source = 'Ballard'
    target = 'Columbia City'
    astar = myastar(graph, source, target)
    print(astar)
    colors = ['red' if edge in astar else 'blue' for edge in graph.edges()]
    markers = ['green' if node in [source, target] else 'blue' for node in graph.nodes()]
    fig, axe = plt.subplots(figsize=(12, 7))
    axe.set_title(f"A*: Total cost of the final path: {astar[1]}", loc='right')
    nx.draw(graph, ax = axe, edge_color = colors, node_color = markers, with_labels=True)
    plt.savefig("example_astar.png")
    # plt.show()

    source = 'West Seattle'
    target = 'Magnolia'
    astar = myastar(graph, source, target)
    print(astar)
    colors = ['red' if edge in astar else 'blue' for edge in graph.edges()]
    markers = ['green' if node in [source, target] else 'blue' for node in graph.nodes()]
    fig, axe = plt.subplots(figsize=(12, 7))
    axe.set_title(f"A*: Total cost of the final path: {astar[1]}", loc='right')
    nx.draw(graph, ax = axe, edge_color = colors, node_color = markers, with_labels=True)
    plt.savefig("astar.wm.png")

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
    # print(f"Starting BFS from '{source}' to '{target}'")
    # print(f"Initial queue: {list(queue)}")
    while queue:
        node = queue.popleft()
        if node == target:
            # print(f"Target '{target}' found!")
            break
        for neighbor in G[node]:
            if neighbor not in parents:
                parents[neighbor] = node
                queue.append(neighbor)
                # print(f"Added neighbor {neighbor} to the queue")
               
    if target not in parents:
        print(f"Target '{target}' not reachable from '{source}'")
        return()

    path = [target]
    while parents[target] is not None:
        path.insert(0, parents[target])
        target = parents[target]

    print(f"Path found: {path}, {len(path)-1}")
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
    
    return path, len(path)-1

def euclidean_distance(G, source, target):
    x1, y1 = G.nodes[source]
    x2, y2 = G.nodes[target]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

@nx._dispatchable(edge_attrs="weight", preserve_node_attrs="heuristic")
def myastar(G, source, target, heuristic=None, weight="weight", *, cutoff=None):
    """
    Return the list of nodes in the path and total cost like ([1,2,3],9)
    """
    if source not in G or target not in G:
        msg = f"Either source {source} or target {target} is not in G"
        raise nx.NodeNotFound(msg)

    if heuristic is None:
        # The default heuristic is h=0 - same as Dijkstra's algorithm
        def heuristic(u, v):
            return 0

    push = heappush
    pop = heappop
    weight = _weight_function(G, weight)

    G_succ = G._adj

    c = count()
    queue = [(0, next(c), source, 0, None)]

    enqueued = {}
    explored = {}

    while queue:
        _, __, curnode, dist, parent = pop(queue)

        if curnode == target:
            path = [curnode]
            node = parent
            while node is not None:
                path.append(node)
                node = explored[node]
            path.reverse()
            return path, dist

        if curnode in explored:
            if explored[curnode] is None:
                continue

            # Skip bad paths that were enqueued before finding a better one
            qcost, h = enqueued[curnode]
            if qcost < dist:
                continue

        explored[curnode] = parent

        for neighbor, w in G_succ[curnode].items():
            cost = weight(curnode, neighbor, w)
            if cost is None:
                continue
            ncost = dist + cost
            if neighbor in enqueued:
                qcost, h = enqueued[neighbor]
                if qcost <= ncost:
                    continue
            else:
                h = heuristic(neighbor, target)

            if cutoff and ncost + h > cutoff:
                continue

            enqueued[neighbor] = ncost, h
            push(queue, (ncost + h, next(c), neighbor, ncost, curnode))
    raise nx.NetworkXNoPath(f"Node {target} not reachable from {source}")

    # pass

### Do NOT remove the following lines of code
if __name__ == "__main__":
    main()