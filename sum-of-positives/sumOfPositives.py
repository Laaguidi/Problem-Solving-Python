def sum_of_positive(arr):
    # Filter out positive elements from the array using a lambda function.
    #The lambda function checks if each element is greater than 0. The filter() function returns an iterator containing only the elements for which the lambda function returns True.
    positive_numbers = filter(lambda x: x > 0, arr)

    # Use the built-in sum function to sum up all positive elements.
    return sum(positive_numbers)


print(sum_of_positive([1, -3, 5, 9]))