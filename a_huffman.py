# huffman.py
## author - nick s.
### get huffman to work first here, then make it into a function for the analysis

# the input, what we want to encode
message: str = 'Hello there'

# the output, should be all 0's and 1s
result: str = str()

# for counting the letter frequencies
freq: dict = dict() # key  -> a letter
                    # item -> num of occurences

# for holding the nodes of the huffman tree
nodes: list = list() 

# for storing the code for each letter
coding: dict = dict()   # key  -> a letter
                        # item -> a binary encoding


# defining our data structures
class Node:
    def __init__(self, weight: int, letter: str, left = None, right = None):
        self.weight: int = weight
        self.letter: str = letter

        self.left: Node = left
        self.right: Node = right

    def __repr__(self):
        return f'Node({self.weight}, {self.letter})'


# recursively traverses the huffman tree to record the codes
def retrieve_codes(v: Node, path: str=''):
    global coding

    if v.letter != None:
        coding[v.letter] = path
    else:
        # Traverse left
        retrieve_codes(v.left, path + '0')

        # Traverse right
        retrieve_codes(v.right, path + '1')


for letter in message:
    if not (letter in freq):
        freq[letter] = 0

    freq[letter] += 1


# STEP 2
## initialize the nodes - TODO
nodes = [Node(value, entry) for entry, value in freq.items()]

# STEP 3 - TODO
## combine each nodes until there's only one item in the nodes list
while len(nodes) > 1:
    ## sort based on weight
    nodes.sort(key=lambda x: x.weight, reverse=True)

    ## get the first min
    min_a: Node = nodes.pop()

    ## get the second min
    min_b: Node = nodes.pop()

    ## combine the two
    combined: Node = Node(min_a.weight + min_b.weight, None)
    combined.left = min_a
    combined.right = min_b

    ## put the combined nodes back in the list of nodes
    nodes.append(combined)

# STEP 4
## reconstruct the codes
huff_root = nodes[0]
retrieve_codes(huff_root)
result: str = ''.join([coding[letter] for letter in message])


# STEP 5
## analyize compression performance
n_original_bits: int = len(message) * 8
n_encoded_bits: int = len(result)
compression_ratio: float = (1 - n_encoded_bits / n_original_bits) * 100

print(f'original: {n_original_bits:^4d} bits')
print(f'encoded : {n_encoded_bits:^4d} bits')
print(f'savings : {int(compression_ratio):^4d} % compression')