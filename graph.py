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

print("The graph")
pp(graph)


def is_jonny(person):
    """Returns true if person is the string jonny

    Arguments:
        person {str} -- the string to be compared

    Returns:
        bool -- the result of comparison
    """
    return person == "jonny"


def search(name):
    """Used the breadth-first-search algorithm to find the minimum possible path to a node

    Arguments:
        name {str} -- the node to start the search from

    Returns:
        bool -- True if found and false otherwise
    """
    search_queue = deque()
    search_queue += graph[name]

    # to keep track of who has been searched
    searched = []

    while search_queue:
        current_person = search_queue.popleft()

        # if person has not been searched
        if not current_person in searched:
            if is_jonny(current_person):
                print(f"{current_person} found!")
                return True
            else:
                # add the neighbouring nodes of the current_person to the queue
                search_queue += graph[current_person]

                # mark current_person as searched
                searched.append(current_person)

    return False


print(search("you"))
