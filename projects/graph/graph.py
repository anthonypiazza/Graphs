# TODO DFS AND DFT RECURSION

"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        # Create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue(starting_vertex)
        # Create an empty Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # If that vertex has not been visited...
            if v not in visited:    
                # Mark it as visited
                # print(v)
                visited.add(v)
                # Then add all of its neighbors to the back of the queue
                for neighbor in self.vertices[v]:
                    q.enqueue(neighbor)
        return visited


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack and push the starting vertex ID
        s = Stack()
        s.push(starting_vertex)
        # Create an empty Set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # If that vertex has not been visited...
            if v not in visited:    
                # Mark it as visited
                # print(v)
                visited.add(v)
                # Then add all of its neighbors to the top of the stack
                for neighbor in self.vertices[v]:
                    s.push(neighbor)
        return visited



                

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        queue = Queue()
        queue.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while queue.size() > 0:
            # Dequeue the first PATH
            path = queue.dequeue()
            # Grab the last vertex from the PATH
            vertex = path[-1]
            # If that vertex has not been visited...
            if vertex not in visited:
                # Here is the point to do whatever we are trying to accomplish
                # Check if its the target
                if vertex == destination_vertex:
                    return path
                # Then add A PATH TO its neighbors to the back of the queue
                visited.add(vertex)
                for neighbor in self.get_neighbors(vertex):
                    # COPY THE PATH
                    path_copy = path.copy()
                    # APPEND THE NEIGHBOR TO THE BACK
                    path_copy.append(neighbor)
                    queue.enqueue(path_copy)        
        # TODO HANDLE WHEN DESTINATION NOT FOUND        
        return None       


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        visited = set()
        stack.push( [starting_vertex] )
        while stack.size() > 0:
            path = stack.pop()
            vertex = path[-1]
            if vertex not in visited:
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                for next_vert in self.vertices[vertex]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    stack.push(new_path)
        return None     # TODO HANDLE WHEN DESTINATION NOT FOUND

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order beginning from starting_vertex.
        No need for data structure (queue or stack)
        This should be done using recursion.
        set has faster lookup time than lists and doesnt allow duplicates
        """
        # {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
        # Initialize visited, if it hasnt been initialized yet
        if visited is None:
            visited = set()
        # If the vertex has not been visited
        if starting_vertex not in visited:
            # Mark the vertex as visited
            # print(starting_vertex)
            visited.add(starting_vertex)
            # Call dft_recursive on each neighbor
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)
        return visited

    def dfs_recursive(self, starting_vertex, target_vertex, visited=None, path = None):
        """
        Return a list containing a path from starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """

        # Init visited
        # 
        if visited is None:
            visited = set()
        # initi path
        if path is None:
            path = []
        visited.add(starting_vertex)
        # Add vertex to path
        path = path + [starting_vertex]
        # If we are at the target value return the path
        if starting_vertex == target_vertex:
            return path
        # Otherwise call dfs.recursive() on each unvisited neighbor
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, target_vertex, visited, path)
                if new_path is not None:
                    return new_path
        return None
        # If the vertex has not been visited


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


    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7


    Valid BFS path:
        [1, 2, 4, 6]


    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''    

    print(f"Graph Vertices: {graph.vertices}")    
    print(f"BFT: {graph.bft(1)}")
    print(f"DFT: {graph.dft(1)}")
    print(f"BFS: {graph.bfs(1, 6)}")
    print(f"DFS: {graph.dfs(1, 6)}")
    print(f"DFT recursive: {graph.dft_recursive(1)}")
    print(f"DFS Recursive: {graph.dfs_recursive(1, 6)}")