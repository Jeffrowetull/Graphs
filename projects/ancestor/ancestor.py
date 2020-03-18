test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
from graph import Graph
from util import Stack, Queue
def earliest_ancestor(ancestors, starting_node):
    print('ancestors:',ancestors)
    print('starting node:',starting_node)
    a_graph = Graph()
    print('a_graph.verts', a_graph.vertices)
    for ancestor in ancestors:
        print('ancestor', ancestor)
        a_graph.add_vertex(ancestor[0])
        a_graph.add_vertex(ancestor[1])
    for ancestor in ancestors:
        a_graph.add_edge(ancestor[1],ancestor[0])
    print('a_graph.verts', a_graph.vertices)
    #bfs
    q = Queue()
    q.enqueue([starting_node])
    path_length = 1
    earliest_ancestor = -1
    while q.size() > 0:
        path = q.dequeue()
        checker = path[-1]
        if (len(path) >= path_length and checker < earliest_ancestor) or (len(path) > path_length):
            earliest_ancestor = checker
            path_length = len(path)
        for neighbor in a_graph.get_neighbors(checker):
            new_path = path.copy()
            new_path.append(neighbor)
            q.enqueue(new_path)
    return earliest_ancestor
print('Ancestor:',earliest_ancestor(test_ancestors, 3))