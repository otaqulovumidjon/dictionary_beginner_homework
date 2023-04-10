def get_max_age_user_name(data:list) -> str:
    """
    Return the name of the user with the maximum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the maximum age in the dictionary
    """
    ls = []
    for i in data:
        ls.append(i["age"])

    m = 0
    for s in ls:
        if s > m:
            m = s
    n = ls.index(m)
    return data[n]["name"]
print(get_max_age_user_name(
    [
  {
    'name': 'John', 
    'age': 32
  }, 
  {
    'name': 'Mary', 
    'age': 18
  }, 
  {
    'name': 'Ann', 
    'age': 20
  }, 
  {
    'name': 'Ban', 
    'age': 29
  }
]))