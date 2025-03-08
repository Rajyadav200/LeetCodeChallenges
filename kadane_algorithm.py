#  
def kadana_algorithm(nums):
    # Initialize the current and global maximum sum with the first element
    current_max = global_max = nums[0]
    
    # Iterating list starting from the second element
    for num in nums[1:]
        # Update current_max by comparing the current element and the sum of current element with current_max
        if current_max + num > num:
            current_max += num
        else:
            current_max = num
        
        # Update global_max if current_max is greater than global_max
        if current_max > global_max:
            global_max = current_max
    
    # Return the global maximum sum
    return global_max

# Define the array
arr = [2, -5, 1, -4, 3, -2]

# Call the function to find the maximum subarray sum
max_subarray_sum = kadana_algorithm(arr)

# Print the result
print(max_subarray_sum)

