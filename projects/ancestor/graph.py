"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise ValueError('vertex does not exist')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError('neighbors not found')

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #create a queue
        q = Queue()
        #enque the starting vertex
        q.enqueue(starting_vertex)
        #create a set to store visitedvertisices
        bft_set = set()
        #while que is not empty
        while q.size() > 0:
            #deque the first vertex
            checker = q.dequeue()
            #check if it's been visited
            if checker not in bft_set:
            #if it hasn't been visited
                print(checker)
                bft_set.add(checker)
                #mark it as visited
                #enque all of its neighbors
                for neighbor in self.get_neighbors(checker):
                    q.enqueue(neighbor)
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #create a stack
        s = Stack()
        #push the starting vertex
        s.push(starting_vertex)
        #create a set to store visitedvertisices
        dft_set = set()
        #while stack is not empty
        while s.size() > 0:
            #pop the last vertex
            checker = s.pop()
            #check if it's been visited
            if checker not in dft_set:
            #if it hasn't been visited
                dft_set.add(checker)
                print(checker)
                #mark it as visited
                #push all of its neighbors
                for neighbor in self.get_neighbors(checker):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        # check if the node has been visited
    
        visited.add(starting_vertex)
        print(starting_vertex)
        #mark it as visited
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor,visited)
        #call dft_recursive on each neighbor

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #create a queue
        q = Queue()
        #enqueue a path to the starting vertex
        q.enqueue([starting_vertex])
        #create a set to tstore visited vertices
        visited = set()
        #while the queue is not empty
        while q.size() > 0:
            #dequeue the first path
            path = q.dequeue()
            #grab the vertex from the end of the path
            checker = path[-1]
            #check if visited
            if checker not in visited:
            #if it hasn't been visited
                #mark as visited
                visited.add(checker)
                #check if it's the target
                if checker == destination_vertex:
                    #if so, return path
                    return path
                #enqueue a path to all of it's neighbors
                for neighbor in self.get_neighbors(checker):
                    new_path = path.copy()
                    new_path.append(neighbor)
                    q.enqueue(new_path)
                #make a copy of the path
                #enqueue the copy

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        #create a stack
        s = Stack()
        #enstack a path to the starteing vertex
        s.push([starting_vertex])
        #create a set to tstore visited vertices
        visited = set()
        #while the stack is not empty
        while s.size() > 0:
            #destack the first path
            path = s.pop()
            #grab the vertex from the end of the path
            checker = path[-1]
            #check if visited
            if checker not in visited:
            #if it hasn't been visited
                visited.add(checker)
                #mark as visited
                if checker == destination_vertex:
                    return path
                #enstack a path to all of it's neighbors
                for neighbor in self.get_neighbors(checker):
                    new_path = path.copy()
                    new_path.append(neighbor)
                    s.push(new_path)
                #make a copy of the path
                #enstack the copy

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if starting_vertex not in visited:
            visited.add(starting_vertex)
        if path is None:
            path = []
        path = path + [starting_vertex]
        if starting_vertex == destination_vertex:
            return path
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                if new_path:
                    return new_path

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
