## Data Structures and Algorithms
This project contains the implementation of a collection of various data structures and algorithms. These are split into two categories: Specific use-case and general algorithms. I developed the specific use-case algorithms myself to solve specific problems I had. I'm sure other similar implementations probably exist, as these problems are not particularly novel. The general algorithms are just practice implementations of commonly used algorithms. Currently, the implemented structures and algorithms include: 

## Specific Use-Case Algorithms
#### Compression Algorithms
- 6-bit string compression (for usernames)
    - Takes standard utf-8 encoded string with a username and encodes it to a 6-bit compressed string. 
    - Many usernames are case insensitive and only allow certain special characters, allowing a full character representation in 6 bits rather than 8
    - I created this algorithm to compress usernames for storage of PySpark DataFrames
    - Average compression of 23% with 0 data loss

## General Algorithms Practice
#### Search Algorithms
- Linear Search: O(n)
- Binary Search: O(log n)

#### Sorting Algorithms
- Bubble Sort: O(n²)
