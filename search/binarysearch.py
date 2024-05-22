# Binary Search function
def binary_search(arr: list, target: float) -> int:
    # Return not found for empty array
    if len(arr) < 1:
        return -1

    # Starting indices for first and last element
    low = 0
    high = len(arr) - 1

    # Iterate until start and end are equal
    while low <= high:
        # Midpoint between start and end
        mid = (low + high) // 2
        # Target is greater than midpoint
        if arr[mid] < target:
            low = mid + 1
        # Target is less than midpoint
        elif arr[mid] > target:
            high = mid - 1
        # Target found
        else:
            return mid
    # Target not found
    return -1


def test_binary_search():
    # Test cases for binary search
    test_cases = [
        # Empty array and target not found
        ([], 5, -1),
        # Single element array and target found
        ([5], 5, 0),
        # Single element array and target not found
        ([5], 7, -1),
        # Multiple elements, target at the beginning
        ([1, 3, 5, 7], 1, 0),
        # Multiple elements, target in the middle
        ([1, 3, 5, 7, 9, 11, 13, 15], 11, 5),
        # Multiple elements, target at the end
        ([1, 3, 5, 7], 7, 3),
        # Multiple elements, target not found (between elements)
        ([1, 3, 5, 7, 9, 11, 13, 15], 8, -1),
        # Multiple elements with duplicates, target found
        ([2, 2, 3, 4, 4, 5, 5, 6], 4, 3),
        # Target greater than all elements
        ([1, 3, 5, 7, 9, 11], 13, -1),
        # Target less than all elements
        ([5, 7, 9, 11, 13], 2, -1),
    ]

    # Colored output message
    success_msg = '\033[92m' + 'Success' + '\x1b[0m'
    failed_msg = '\033[91m' + 'Failed' + '\x1b[0m'
    for i, (data, target, expected) in enumerate(test_cases):
        result = binary_search(data, target)  # Replace with your binary_search function
        success = result == expected
        print(f"Test Case {i+1}: {success_msg if success else failed_msg} - Expected: {expected}, Got: {result}")

# Run the test cases
test_binary_search()