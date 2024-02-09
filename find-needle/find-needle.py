def find_needle(arr):
    # Define a function called find_needle which takes an array 'arr' as input

    # Use the index method to find the index of the first occurrence of the string "needle" in the array
    index = arr.index("needle")

    # Return a string indicating the position where "needle" was found by concatenating the index
    # with the message "found the needle at position "
    return f"found the needle at position {index}"


# Call the function find_needle with an example array and print the result
print(find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]))