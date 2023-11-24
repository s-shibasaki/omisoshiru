def convert_list_of_dicts_to_dict_of_lists(list_of_dicts):
    keys, values = zip(*[zip(*i.items()) for i in list_of_dicts])
    dict_of_lists = {k: v for k, v in zip(keys[0], zip(*values))}
    return dict_of_lists
