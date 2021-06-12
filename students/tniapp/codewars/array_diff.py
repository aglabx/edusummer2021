def array_diff(list1, list2):
    new_list = []
    [new_list.append(i) for i in list1 if i not in list2]
    return new_list
