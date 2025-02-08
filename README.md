# Huffman Encoding and Decoding in Python

This repository contains a Python implementation of the **Huffman Encoding** algorithm, a lossless data compression technique. The implementation includes building a Huffman tree, generating Huffman codes, encoding text, and decoding the encoded text back to the original.

## Table of Contents

- [Huffman Encoding and Decoding in Python](#huffman-encoding-and-decoding-in-python)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Decoding Text](#decoding-text)
  - [Example](#example)
  - [Testing](#testing)
  - [Acknowledgments](#acknowledgments)

## Overview

Huffman Encoding is a widely used algorithm for lossless data compression. It works by assigning variable-length codes to input characters, with shorter codes assigned to more frequent characters. This repository provides a Python implementation of the algorithm, including:

- Building a Huffman tree from input text.
- Generating Huffman codes for each character.
- Encoding text using the generated Huffman codes.
- Decoding the encoded text back to the original.

## Features

- **Huffman Tree Construction**: Builds a Huffman tree based on character frequencies.
- **Huffman Code Generation**: Generates binary codes for each character in the input text.
- **Text Encoding**: Encodes input text using the generated Huffman codes.
- **Text Decoding**: Decodes the encoded text back to the original text.
- **Unit Tests**: Includes comprehensive unit tests to ensure correctness.

## Installation

To use this implementation, clone the repository to your local machine:

```bash
git clone https://github.com/your-username/huffman-encoding.git
cd huffman-encoding
```

## Usage
Encoding Text
To encode a text string using Huffman Encoding:

```python
from huffman import build_huffman_tree, build_huffman_table, huffman_encode

text = "ABCDABCC"
root = build_huffman_tree(text)
huffman_table = build_huffman_table(root)
encoded_text = huffman_encode(text, huffman_table)

print(f"Encoded Text: {encoded_text}")
```

## Decoding Text
To decode the encoded text back to the original:

```python
from huffman import huffman_decode

decoded_text = huffman_decode(encoded_text, huffman_table)
print(f"Decoded Text: {decoded_text}")
```

## Example
```python
text = "ABCDABCC"
root = build_huffman_tree(text)
huffman_table = build_huffman_table(root)
encoded_text = huffman_encode(text, huffman_table)
decoded_text = huffman_decode(encoded_text, huffman_table)

print(f"Original Text: {text}")
print(f"Encoded Text: {encoded_text}")
print(f"Decoded Text: {decoded_text}")
```

Output:
```
Original Text: ABCDABCC
Encoded Text: 1001011100111
Decoded Text: ABCDABCC
```

## Testing
The repository includes a suite of unit tests to ensure the correctness of the implementation. To run the tests, use the following command:

```bash
python -m unittest test_huffman.py
```

Test Cases
The tests cover the following scenarios:

1. Building the Huffman tree.
2. Generating the Huffman table.
3. Encoding text using Huffman codes.
4. Decoding encoded text back to the original.
5. Handling edge cases (empty input and single-character input).

## Acknowledgments
The Huffman Encoding algorithm was introduced by David A. Huffman in 1952.

This implementation is based on Python's standard library modules (heapq, collections).