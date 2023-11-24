def convert_dict_of_lists_to_list_of_dicts(dict_of_lists):
    """
    Convert a dictionary of lists to a list of dictionaries with the same keys.

    Parameters
    ----------
    dict_of_lists : dict
        A dictionary where the values are lists.

    Returns
    -------
    list of dict
        A list of dictionaries with the same keys as the input dictionary, where the values are taken from the corresponding list in the input dictionary.
    """
    keys, values = zip(*dict_of_lists.items())
    list_of_dicts = [{k: v for k, v in zip(keys, item)} for item in list(zip(*values))]
    return list_of_dicts
