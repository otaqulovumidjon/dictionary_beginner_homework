def find_max_key(data: dict):
    """
    Return the maximum int or float key in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum key in the dictionary.
    """
    ls = []
    js = []
    for i in data.keys():
        ls.append(i)

    m = 0
    for n in ls:
        if n > m:
            m = n
    return m
print(find_max_key({1: 'a', 2: 'b', 3: 'c'}))