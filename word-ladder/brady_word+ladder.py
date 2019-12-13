f = open('words.text', 'r')
words = f.read().split("\n")
f.close()

word_set = set()

for word in words:
    word_set.add(word.lower())


def get_neighbors(word):
    '''
    Return all words from word_liat that are exactly 1 letter different
    ''' 
    # OPTION 1:
    
    # For each word in our word list...
        # If words are not the same length, continue
        # Check letter by letter
        # Break once different letters > 1
            # Time Complexity: O(number_words * length_of_begin_word)
            # Space Complexity: O(number_words)
    
    # OPTION 2: ----> Utilize hashtable to speed it up see Option 2.1
    # For each letter in our word, check each other letter and..
    # See if that word is in the set
            # Time Complexity: O(26 * length_of_begin_word * number_words)
            # Space Complexity: O(number_words)

    # Option 2.1: word_list is now a set() --- O(number_words)
            # Time Complexity: O(length_of_begin_word)
            # Space Complexity: O(number_words)

    # Option 2.1 Implmentation
    # Return all words from word_liat that are exactly 1 letter different


    neighbors = []

    letter_list = list(word) # "abc" -> ['a', 'b', 'c']

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # For each letter in our word...
    for i in range(len(letter_list)):
        
        # Check each other letter
        for letter in letters:
            temp_word = list(letter_list)
            temp_word[i] = letter
            w = "".join(temp_word)
            
            # And see if that word is in the set
            if w != word and w in word_set:
                # If so, add to return the list
                neighbors.append(w)
    
    return neighbors
    

def word_ladder_path(self, begin_word, end_word):
    queue = Queue()
    queue.enqueue([begin_word])
    visited = set()
    while queue.size() > 0:
        path = queue.dequeue()
        vertex = path[-1]
        if vertex not in visited:
            if vertex == end_word:
                return path
            visited.add(vertex)
            for neighbor in self.get_neighbors(vertex):
                path_copy = path.copy()
                path_copy.append(neighbor)
                queue.enqueue(path_copy)
    return None

print(word_ladder_path("hit", "cog"))