def get_user_names_with_age_range(data:list, min_age:int, max_age:int) -> list:
    """
    Return a list of users with a given age range

    Args:
        data (dict): A dictionary of values
        min_age (int): The minimum age to search for
        max_age (int): The maximum age to search for
    Returns:
        list: A list of users with the given age range
    """
    ls = []
    js = []

    for i in data:
        ls.append(i["age"])

    for n in ls:
        if min_age < n and n < max_age:
            s = data[ls.index(n)]['name']
            js.append(s)
    return js

print(get_user_names_with_age_range([
  {
    'name': 'John', 
    'age': 20
  }, 
  {
    'name': 'Mary', 
    'age': 17
  },
  {
    'name': 'Ban', 
    'age': 23
  },
  {
    'name': 'John', 
    'age': 27
  }
], 18, 25))