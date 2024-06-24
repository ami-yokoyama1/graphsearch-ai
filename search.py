import matplotlib.pyplot as plt
import networkx as nx
import random
import csv 
import pandas as pd

"""
These are Function Headers
Complete the functions to ensure they return expected results
Replace these comments with documenation about the program
@author [add your name]
"""

with open('./graph.csv', newline='') as csvfile:
    routes_us = pd.read_csv(csvfile)
    

graph = nx.from_pandas_dataframe(routes_us, source = 'Source Airport', target = 'Dest Airport',
                        edge_attr = 'number of flights',create_using = nx.DiGraph())

def mybfs(G, source, target):
    """
    Return the searched edges as list of tuples
    """
    pass #pass is a placeholder for an empty function, you will need to remove this
    
def mydfs(G, source, target):
    """
    Return the searched edges as list of tuples
    """
    pass

def myastar(G, source, target):
    """
    Return the list of nodes in the path and total cost like ([1,2,3],9)
    """
    pass

def main():
    """
    Main body of your code below.
    """
    pass

### Do NOT remove the following lines of code
if __name__ == "__main__":
    main()