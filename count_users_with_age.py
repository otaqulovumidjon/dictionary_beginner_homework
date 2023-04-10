def count_users_with_age(data:list, age:int) -> int:
    """
    Return the number of users with a given age

    Args:
        data (dict): A dictionary of values
        age (int): The age to search for
    Returns:
        int: The number of users with the given age
    """
    s = 0
    for i in data:
        if i["age"] == age:
            s += 1 
    return s
print(count_users_with_age([{"name":"Umidjon", "age":20}, {"name":"Husan", "age":22}], ))