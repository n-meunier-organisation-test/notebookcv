def convert(my_name):
    """
    Print a line about converting a notebook.
    :param my_name: str: person's name
    :return: None
    """
    try:
        print(f"I will convert a notebook for you some day, {str(my_name)}.")
    except TypeError:
        print('Caught TypeError Exception')
