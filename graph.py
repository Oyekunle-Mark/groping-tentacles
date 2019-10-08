from pprint import pprint as pp
from collections import deque

# use a hash table to hold the graph
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

pp(graph)

search_queue = deque()
search_queue += graph["you"]
