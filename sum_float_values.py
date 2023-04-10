def sum_float_values(data: dict) -> float:
    '''
    Return the sum of all float values in dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        float: The sum of all float values in the dictionary.
    '''
    s = 0
    for i in data.values():
        if i != int(i):
            s += i
    return s
print(sum_float_values({
    1: 22.4, 
    2: 3.5, 
    3: 1, 
    4: 7.6, 
    5: 2, 
    6: 3
  }))