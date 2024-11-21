 # MinHeap Project

This project implements a MinHeap data structure in Python. The MinHeap class allows you to insert elements, extract the minimum element, and perform other heap operations.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [Structure](#structure)

## Installation

To use the MinHeap class, you need to have Python installed on your machine. You can clone this repository and use the `heap.py` file directly.

```sh
git clone https://github.com/BgYana/min-heap
cd min-heap
```


## Usage
The MinHeap class provides the following methods:

- **insert(value):** Inserts a value into the heap.
- **extract_min():** Extracts and returns the minimum value from the heap.
- **get_min():** Returns the minimum value from the heap without removing it.
- **is_empty():** Returns True if the heap is empty, False otherwise.
- **size():** Returns the number of elements in the heap.

# Example
```python
from heap import MinHeap

# Create a MinHeap instance
min_heap = MinHeap()

# Insert elements into the heap
min_heap.insert(20)
min_heap.insert(3)

# Get the minimum element
print("Minimum element:", min_heap.get_min())  # Output: 3

# Extract the minimum element
print("Extracted minimum element:", min_heap.extract_min())  # Output: 3

# Check if the heap is empty
print("Is the heap empty?", min_heap.is_empty())  # Output: False

# Get the size of the heap
print("Size of the heap:", min_heap.size())  # Output: 1
```
# Testing

The project includes a test.py file with unit tests for the MinHeap class.
You can run the tests using the following command:
```sh
python -m unittest test.py
```
# Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or improvements.

# Structure

```
minheap/
├── heap.py
├── test.py
├── README.md
└── LICENSE
```