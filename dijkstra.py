from pprint import pprint as pp

# build the graph
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

pp(graph)

# hash table for the cost
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# hash table for parents
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# to check if a node has been processed
processed = []
