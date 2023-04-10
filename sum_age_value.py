def sum_age_values(data:list) -> int:
    """
    Return the sum of all age values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of all age values in the dictionary
    """
    ls = []
    for i in data:
        ls.append(i['age'])

    s = 0
    for n in ls:
        s += n
    return s
print(sum_age_values([
  {
    'name': 'John', 
    'age': 27
  }, 
  {
    'name': 'Mary', 
    'age': 42
  }
]))