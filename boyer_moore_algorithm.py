#   This Python script implements the Boyer-Moore Voting algorithm to find prime numbers within a given range.
#   Time complexity: O(n)
#   Space complexity: O(1)
def majority_element(nums):

    """
    This function identifies the majority element in a list using the Boyer-Moore Voting Algorithm.
    
    Parameters:
        numbers (list): A list of integers.

    Returns:
        int: The majority element (if one exists).
    """

    # Initialize the count and candidate variables
    vote_count, majority_candidate = 0, None

    # Voting phase: find a majority elements occures more than n//3
    for num in nums:
        if vote_count == 0: 
            majority_candidate = num
        vote_count += 1 if majority_candidate == num else -1

    return majority_candidate

# Example array
arr = [1, 2, 4, 5, 4, 2, 4, 1]

# Find the majority element
ele = majority_element(arr)
print("The majority element is:", ele)
