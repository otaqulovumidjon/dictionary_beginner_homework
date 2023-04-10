def find_max_value(data: dict):
    """
    Return the maximum int or float value in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum value in the dictionary.
    """
    ls = []
    m = 0
    for i in data.values():
        # ls.append(i)
        if i > m:
            m = i

    return i
print(find_max_value({'a' : 1, 'b' : 2, 'c' : 3}))