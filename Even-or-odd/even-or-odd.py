def even_or_odd(number):
    # Use a conditional (ternary) expression to check if the remainder of 'number' divided by 2 is 0
    # If true, assign the string "even" to the variable 'result'; otherwise, assign "odd"
    result = "even" if number % 2 == 0 else "odd"
    # Return the calculated result ("even" or "odd") from the function
    return result
# Call the even_or_odd function with the argument 11 and print the result
print(even_or_odd(11))