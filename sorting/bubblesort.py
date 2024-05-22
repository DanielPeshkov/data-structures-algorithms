# Bubble Sort function
def bubble_sort(arr: list) -> list:
    # Iterate over each item in list
    for i in range(len(arr)):
        # Iterate over each item before i
        for j in range(len(arr)-i-1):
            # Compare j to next item and switch if j is larger
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


def test_bubble_sort():
    # Test cases with different data types and sizes
    test_cases = [
        ([], []),                                  # Empty list
        ([1], [1]),                                # Single element list
        ([3, 1, 4, 1, 5], [1, 1, 3, 4, 5]),        # Unsorted list
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),        # Already sorted list
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),        # Reverse sorted list
        ([2, 1, 2, 1, 2], [1, 1, 2, 2, 2]),        # List with duplicates
        ([-1, -7, -3], [-7, -3, -1]),              # List with negative numbers
        (list(range(10)), list(range(10))),        # List with increasing order
        (list(range(10, 0, -1)), sorted(range(10, 0, -1))), # List with decreasing order
        ([3, 3, 3], [3, 3, 3]),                   # List with all elements the same
    ]

    # Colored output message
    success_msg = '\033[92m' + 'Success' + '\x1b[0m'
    failed_msg = '\033[91m' + 'Failed' + '\x1b[0m'
    for i, (data, expected) in enumerate(test_cases):
        sorted_data = bubble_sort(data.copy())  # Copy to avoid modifying original data
        success = sorted_data == expected
        print(f"Test Case {i+1}: {success_msg if success else failed_msg} - Expected: {expected}, Got: {sorted_data}")

test_bubble_sort()