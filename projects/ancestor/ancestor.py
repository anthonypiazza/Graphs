# 1. Understand the problem
#     - Node: numbers/people
#     - Edges: parent-child relationship
#     - Undirected
#     - Acyclic
#     - Sparse
#     - DFT --> furthest

# 2. Implement the Graph

# 3. Traverse the Graph

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def earliest_ancestor(ancestors, starting_node):
    s = Stack()
    s.push(starting_node)
    visited = set()
    first_ancestor = -1
    print(ancestors)

    # While stack has ancestors
    while s.size() > 0:
        # pop ancestor
        v = s.pop()
        # if ancestor has not been visited
        if v not in visited:
            # Add to visited
            visited.add(v)
            print(visited) 
            
            for ancestor in ancestors:
                
                if ancestor[1] == v:
                    s.push(ancestor[0])

                    if first_ancestor == -1:
                        first_ancestor = ancestor[0]
                        # print(F"First Ancestor: {first_ancestor}")
                    
                    parents = []

                    for a in ancestors:
                        if a[1] == v:
                            parents.append(a[0])

                            if len(parents) == 1:
                                first_ancestor = a[0]
                            else:
                                if first_ancestor > a[0]:
                                    first_ancestor = a[0]
                                # print(F"First Ancestor: {first_ancestor}")
        
    print(first_ancestor)
    return first_ancestor

