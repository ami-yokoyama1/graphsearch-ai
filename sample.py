import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


pd.options.display.max_columns = 20
import numpy as np
rng = np.random.RandomState(seed=5)
ints = rng.randint(1, 11, size=(3, 2))
a = ["A", "B", "C"]
b = ["D", "A", "E"]
df = pd.DataFrame(ints, columns=["weight", "cost"])
df[0] = a
df["b"] = b
df[["weight", "cost", 0, "b"]]

G = nx.from_pandas_edgelist(df, 0, "b", ["weight", "cost"])
G["E"]["C"]["weight"]
10
G["E"]["C"]["cost"]
9
edges = pd.DataFrame(
    {
        "source": [0, 1, 2],
        "target": [2, 2, 3],
        "weight": [3, 4, 5],
        "color": ["red", "blue", "blue"],
    }
)
G = nx.from_pandas_edgelist(edges, edge_attr=True)
G[0][2]["color"]
'red'

nx.draw_networkx(G)
plt.savefig("dist_map.png", format="PNG", dpi = 300)
plt.show()
