from collections import Counter

import json
import heapq
import unittest


class HuffmanNode:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    """
    Builds a huffman tree from the given text
    :returns: the root node of the huffman tree
    """
    if text == "":
        return None

    heap = [HuffmanNode(char, freq) for char, freq in Counter(text).items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)

    root = heapq.heappop(heap)
    return root


def build_huffman_table(node, prefix="", huffman_table=None):
    """
    Builds the huffman table from for the give huffman tree
    """
    # to handle reusing the same dict in other  testcases
    if huffman_table is None:
        huffman_table = {}

    if node:
        if node.char is not None:
            huffman_table[node.char] = prefix
        build_huffman_table(node.left, prefix + "0", huffman_table)
        build_huffman_table(node.right, prefix + "1", huffman_table)

    return huffman_table


def huffman_encode(text, huffman_table):
    encoded_text = "".join(huffman_table[char] for char in text)
    return encoded_text


def huffman_decode(encoded_text, huffman_table):
    inverse_huffman_table = {v: k for k, v in huffman_table.items()}
    temp = ""
    decoded_text = ""
    for bit in encoded_text:
        temp += bit
        if temp in inverse_huffman_table:
            decoded_text += inverse_huffman_table[temp]
            temp = ""

    return decoded_text


class TestHuffmanEncoding(unittest.TestCase):
    def test_build_huffman_tree(self):
        text = "ABCDABCC"
        root = build_huffman_tree(text)
        self.assertIsInstance(root, HuffmanNode)
        self.assertEqual(root.freq, 8)  # Total characters in "ABCDABCC"

    def test_build_huffman_table(self):
        text = "ABCDABCC"
        root = build_huffman_tree(text)
        huffman_table = build_huffman_table(root)
        self.assertIsInstance(huffman_table, dict)
        self.assertEqual(len(huffman_table), 4)  # Unique characters: A, B, C, D

    def test_huffman_encode(self):
        text = "ABCDABCC"
        root = build_huffman_tree(text)
        huffman_table = build_huffman_table(root)
        encoded_text = huffman_encode(text, huffman_table)
        self.assertIsInstance(encoded_text, str)
        self.assertTrue(
            all(bit in "01" for bit in encoded_text)
        )  # Ensure binary encoding

    def test_huffman_decode(self):
        text = "ABCDABCC"
        root = build_huffman_tree(text)
        huffman_table = build_huffman_table(root)
        encoded_text = huffman_encode(text, huffman_table)
        decoded_text = huffman_decode(encoded_text, huffman_table)
        self.assertEqual(decoded_text, text)  # Ensure decoded text matches original

    def test_empty_input(self):
        text = ""
        root = build_huffman_tree(text)
        self.assertIsNone(root)  # No tree for empty input
        huffman_table = build_huffman_table(root)
        self.assertEqual(huffman_table, {})
        encoded_text = huffman_encode(text, huffman_table)
        self.assertEqual(encoded_text, "")
        decoded_text = huffman_decode(encoded_text, huffman_table)
        self.assertEqual(decoded_text, "")

    def test_single_character_input(self):
        text = "AAAAA"
        root = build_huffman_tree(text)
        self.assertEqual(root.freq, 5)  # Only one character
        huffman_table = build_huffman_table(root)
        self.assertEqual(huffman_table, {"A": ""})  # Single character has empty code
        encoded_text = huffman_encode(text, huffman_table)
        self.assertEqual(encoded_text, "")
        decoded_text = huffman_decode(encoded_text, huffman_table)
        self.assertEqual(decoded_text, "")


if __name__ == "__main__":

    text = "ABCDFGABD"
    print(f"input: {text}")

    root = build_huffman_tree(text)
    huffman_table = build_huffman_table(root)
    print("huffman_table:\n", json.dumps(huffman_table, indent=4))

    encoded_text = huffman_encode(text, huffman_table)
    print(f"encoded: {encoded_text}")

    decoded_text = huffman_decode(encoded_text, huffman_table)
    print(f"decoded: {decoded_text}")

    unittest.main()
