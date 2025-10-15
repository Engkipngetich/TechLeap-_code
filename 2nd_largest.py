
# Function to find the second largest number in a list
def second_largest(numbers):
    # Remove duplicates to avoid counting the same number twice
    unique_numbers = list(set(numbers))
    
    # Check if there are at least two unique numbers
    if len(unique_numbers) < 2:
        return None  # No second largest number exists
    
    # Sort the list in descending order
    unique_numbers.sort(reverse=True)
    
    # Return the second item (second largest)
    return unique_numbers[1]

# Example usage
nums = [10, 20, 4, 45, 99, 99]
print(second_largest(nums))  # Output: 45

# Explanation:
# Convert to set → removes duplicate numbers.
# Sort in descending order → so the largest comes first.
# Return the second element → that’s the second-largest number.
# Handle edge cases → if the list has fewer than two unique numbers, return None.
