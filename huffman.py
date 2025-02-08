import heapq
from collections import Counter


class HuffmanNode:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


text = "ABAACZ"
print(f"input: {text}")

# Step 1: Build the frequency dict
# the format v, k is important for heapify
heap = [HuffmanNode(char, freq) for char, freq in Counter(text).items()]
heapq.heapify(heap)


while len(heap) > 1:
    left = heapq.heappop(heap)
    right = heapq.heappop(heap)
    new_node = HuffmanNode(freq=left.freq + right.freq, left=left, right=right)
    heapq.heappush(heap, new_node)

# Log encoding
root = heapq.heappop(heap)

huffman_table = {}


def dfs(node, encoding=""):
    if not node.left and not node.right:
        huffman_table[node.char] = encoding
        return

    dfs(node.left, encoding + "0")
    dfs(node.right, encoding + "1")


dfs(root)
print(f"huffman_table: {huffman_table}")

# Step 3: Encode the string using the prefix
encoded_text = "".join(map(lambda c: huffman_table[c], text))
print(f"encoded_text: {encoded_text}")


# Step 4: Decode the string
def dfs_decode(s, i=0, node=root):
    if not node.left and not node.right:
        return node.char
    if i == len(s):
        return None
    if s[i] == "0":
        return dfs_decode(s, i + 1, node.left)

    return dfs_decode(s, i + 1, node.right)


start, i = 0, 0
decoded_text = ""
while i < len(encoded_text):
    span = encoded_text[start : i + 1]
    char = dfs_decode(span)
    if char:
        decoded_text += char
        start = i + 1
    else:
        i += 1

print(f"ouput: {decoded_text}")
