def get_min_age_user_name(data:list) -> str:
    """
    Return the name of the user with the minimum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the minimum age in the dictionary
    """
    ls = []
    js = []
    for i in data:
        ls.append(i['age'])

    x = 0
    y = 0
    while x < len(ls):
        if ls[x] > y:
            y = ls[x]
        x += 1
    
    n = 0
    while n < len(ls):
        if ls[n] < y:
            y = ls[n]
        n += 1

    h = ls.index(y)
    k = data[h]['name']

    return k

print(get_min_age_user_name([
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