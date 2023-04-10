def count_jobs(data:list, job:str) -> int:
    """
    Return the number of users with a given job

    Args:
        data (dict): A dictionary of values
        job (str): The job to search for
    Returns:
        int: The number of users with the given job
    """
    s = 0
    for i in data:
        if i['job'] == job:
            s += 1
    return s
print(count_jobs([{'name':'Umidjon', 'job':'dasturchi'}, {'name':'Husan', 'job':'dasturchi'}], 'dasturchi'))
# print(count_jobs([{'name': 'John', 'job': 'Developer'}, {'name': 'Mary', 'job': 'Developer'}], 'Developer'))