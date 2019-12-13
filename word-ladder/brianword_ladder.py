# Given two words (beginWord and endWord), and a dictionary's word list, 
# return the shortes transformation sequence from beginWord to endWord.

# such that:

# Only one letter can be changed at atime.
# Each transformed word must exist in the word list. Not the beginWord i???
# transformed word.

# Note:

# Return None if there is no shuc transformation sequence.
# All words have the same length.
# All word contain onlu lowecase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are no the same.

# Sample:
# beginWord = "hit"
# endWord = "cog"
# return: ['hit', 'hot', 'cot', 'cog']

# beginWord = "sail"
# endWord = "boat"
# ['sail', 'bail', 'boil', 'ball', 'bolt', 'boat']

# beginWord = "hungry"
# endWord = "happy"
# None


# Words - vertex
# letters different - edges (part)
# shortest transformation sequnce - path/bfs
# Dictionary - list of vertexes
# beginWorld - starting vertex
# EndWord - destination vertex
# No duplicates - use a set()
# Same length - edges (part)

f = open('words.text', 'r')
words = f.read().split("\n")

word_set = set()

for word in words:
    word_set.add(word.lower())

# Find/create all nodes/edges for words with one letter different
# Replaces entry in the adjacency list for that node

def get_neighbors(word):
    neighbors = []
    string_word = list(word)
    for i in range(0, len(string_word)):
        for letter in list("abcdefghijklmnopqrstuvwxyz"):
            temp_word = list(string_word)
            temp_word[i] = letter
            w = "" join(temp_word)
            if w != word and w in word_set:
                neighbors.append(w)

    return neighbors

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

def find_word_ladder(beginWord, endWord):
        # queue = Queue()
        # visited = set()
        # queue.enqueue([starting_vertex])
        # while queue.size() > 0:
        #     path = queue.dequeue()
        #     vertex = path[-1]
        #     if vertex not in visited:
        #         if vertex == destination_vertex:
        #             return path
        #         visited.add(vertex)
        #         for next_vert in self.vertices[vertex]:
        #             new_path = list(path)
        #             new_path.append(next_vert)
        #             queue.enqueue(new_path)
        queue = Queue()
        visited = set()
        queue.enqueue([beginWord])

        while queue.size() > 0:
            path = queue.dequeue()
            vertex = path[-1] #Vertex is our word
            if vertex not in visited:
                # Heres where we do the thing
                if vertex == end_word:
                    return path
                visited.add(vertex)
                for new_vert in get_neighbors(vertex):
                    new_path = list(path)
                    new_path.append(new_vert)
                    queue.enqueue(new_path)

                    print(find_word_ladder("sail", "boat"))