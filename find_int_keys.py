def find_int_keys(data: dict) -> list:
    """
    Return a list of all keys in a dictionary that are integers.
    Args:
        data (dict): A dictionary of values
    Returns:
        list: A list of all keys in the dictionary that are integers.
    """
    ls = []
    js = []

    for i in data.keys():
        ls.append(i)

    for n in ls:
        if type(n) == int:
            js.append(n)
    return js
print(find_int_keys({"x": "23", 3: "y", "z": "5", 7:'a'}))

# x = {
#     "x": "23",
#     "3": "y", 
#     "z": "5", 
#     7:'a'
#   }
# ls = []
# for i in x.keys():
#     ls.append(i)
# s = tuple(ls)


# js = []
# x = 0
# while x < len(s):
#     if s[x] == int:
#         js.append(s[x])
#     x += 1
# print(js)