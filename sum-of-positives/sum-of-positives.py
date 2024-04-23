def sum_of_positive(arr):
    # The function sum_of_positive takes an array 'arr' as input.

    return sum(x for x in arr if x > 0)
    # This line uses a generator expression inside the sum() function.
    # It iterates over each element 'x' in the input array 'arr'.
    # It filters only the elements that are greater than 0 using the condition 'if x > 0'.
    # The sum() function then calculates the sum of these filtered elements.

print(sum_of_positive([1, -3, 5, 9]))
# Calls the sum_of_positive function with the input array [1, -3, 5, 9] and prints the result.