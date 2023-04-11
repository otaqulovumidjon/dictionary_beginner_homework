def get_user_names_with_age(data:list, age:int) -> list:
    """
    Return a list of users with a given age

    Args:
        data (dict): A dictionary of values
        age (int): The age to search for
    Returns:
        list: A list of users with the given age
    """
    ls = []
    js = []
    for i in data:
        ls.append(i['age'])
    
    n = 0
    while n < len(ls):
        if ls[n] == age:
            js.append(data[n]['name'])
        n += 1
    return js
print(get_user_names_with_age([
  {
    'name': 'John', 
    'age': 30
  }, 
  {
    'name': 'Ann', 
    'age': 32
  }, 
  {
    'name': 'Sam', 
    'age': 27
  }, 
  {
    'name': 'Mary', 
    'age': 32
  }
], 32))


# ls = [30, 32, 27, 32]
# js = []
# for i in ls:
#     if i == 32:
#         js.append(ls.count(i))
# print(js)