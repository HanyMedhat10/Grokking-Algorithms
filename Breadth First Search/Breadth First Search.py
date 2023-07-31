"""
The algorithm works as follows:

1.Create a queue data structure to keep track of the vertices to be visited.
2.Enqueue the starting vertex into the queue.
3.While the queue is not empty, do the following:
a. Dequeue the vertex at the front of the queue.
b. Visit the dequeued vertex.
c. Enqueue all the adjacent vertices of the dequeued vertex that have not been visited yet.
d. Mark the dequeued vertex as visited.
"""
from collections import deque
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj","peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom","jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
search_queue = deque()
search_queue += graph["you"]
def person_is_seller(name):
    return name[-1]=='m'


while search_queue:
    person = search_queue.popleft()
    if person_is_seller(person):
        print(person + "is a mongo seller!")
        # return True
    else:
        search_queue +=graph[person]
# return False
# Chat GPT code
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


