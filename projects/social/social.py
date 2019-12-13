import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)



class User:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self.name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}



    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)




    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()




    def populate_graph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        # avgFriendships = totalFriendships / numUsers
        # totalFriendships = avgFriendships * numUsers
            
        # Add users
        # call addUser( until our number of users is numUsers)
        for i in range(numUsers):
            self.add_user(f"User {i}")
        # Create random friendships
        # Generate a list of all possible friendships
        possibleFriendships = []
        # Avoid dups by ensuring the first ID is smaller than the second
        for userID in self.users:
            for friendID in range(userID + 1, self.last_id + 1):
                possibleFriendships.append( (userID, friendID) )
        print(f"Possible Friendships: {possibleFriendships}")

        # Shuffle the list
        random.shuffle(possibleFriendships)
        # Slice off totalFriendships from the front, create friendships
        totalFriendships = avgFriendships * numUsers // 2
        print(f"Friendships to create: {totalFriendships}\n")
        for i in range(totalFriendships):
            friendship = possibleFriendships[i]
            # Create friendships
            self.add_friendship( friendship[0], friendship[1])
        

# Brady's Populate Graph
    # def populate_graph(self, numUsers, avgFriendships):
    #     '''
    #     - Takes a user's userID as an argument
    #     - Returns a dictionary containing every user in 
    #     that user's extended network with the shortest 
    #     friendship path between them.
    #     - The key is the friend's ID and the value is the path.
    #     '''
        
    #     visited = {} #This is a Dictionary, not set
    #     # Do BFT, store the paths as we go
    #     # Create an empty queue
    #     queue = Queue()
        
    #     # Add a PATH to the starting node to the queue
    #     q.enqueue( [userID] )
    #     # While the queue is not empty...
    #     while queue.size() > 0:
    #         # Dequeue the PATH from the queue
    #         path = queue.dequeue()
    #         vertex = path[-1]    
            
    #         # Check if it's been visited  
    #         if vertex not in visited:
    #             # When we reach an unvisited node, add the path to visited dict
    #             visited[v] = path
    #             # Add a path to each neighbor to the back of the queue
    #             for friendID in self.friendships[vertex]:
    #                 path_copy = path.copy()
    #                 path_copy.append(friendID)
    #                 q.enqueue(path_copy)
    #     # Return visited dictionary
    #     return visited








    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """        
        queue = Queue()
        queue.enqueue( [user_id] )
        visited = {} # Note that this is a dictionary, not a set
        
        visited[user_id] = [user_id]  # { 1: [] }

        while queue.size() > 0:
            print(f"Queue Size: {queue.size()}")
            path = queue.dequeue()  # 1
            vertex = path[-1]  # 1

            print(f"User {vertex} friends: {self.friendships[vertex]}")
            print(f"Visited: {visited}")
            # print(f"Visited exists: {visited[vertex] == []}")

            if vertex not in visited:
                visited[vertex] = path


            for friend in self.friendships[vertex]:
                # print(f"Friend: {friend}")
                if friend not in visited:
                    path_copy = path.copy()
                    path_copy.append(friend)
                    queue.enqueue(path_copy)

        return visited
        
        # Brady's Pseudocode Solution
        # Create an empty queue
        #Add a PATH to the starting node to the queue
        # While queue is not empty...
            # Dequeue the first PATH from the queue
            # Check if its been visited
            # If not, mark it as visited
                # When we reach an unvisited node, add the path to visited dict
            # Add a path to each neighbor to the back of the queue
        # Return visited dictionary

# 1.Understand the problem
    # - Nodes: users
    # - Vertices: friendships
    # - Undirected
    # - Cyclic
    # - Sparse
    # - Breadth - shortest path


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print("Users:")
    print(sg.users)
    print("Friendships:")
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
