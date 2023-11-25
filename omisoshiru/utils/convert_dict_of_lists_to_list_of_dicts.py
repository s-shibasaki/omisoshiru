def convert_dict_of_lists_to_list_of_dicts(dict_of_lists, nest=None):
    if isinstance(nest, int) and nest > 1:
        dict_of_lists = {
            k: convert_dict_of_lists_to_list_of_dicts(v, nest - 1)
            for k, v in dict_of_lists.items()
        }

    keys, values = zip(*dict_of_lists.items())
    list_of_dicts = [{k: v for k, v in zip(keys, item)} for item in zip(*values)]
    return list_of_dicts
