def find_length_of_values(data: dict) -> int:
    """
    Return the sum of the length of all values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of the length of all values in the dictionary.
    """
    ls = []
    js = 0
    for i in data.values():
        ls.append(len(i))

    for s in ls:
        js += s
    return js

print(find_length_of_values({'a': 'abc', 'b': 'def', 'c': 'ghi'}))