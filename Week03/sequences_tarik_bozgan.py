def remove_duplicates(list):
    seen = set()
    result = []
    for item in list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def list_counts(list):
    counts = {}
    for item in list:
        if item in counts:
            counts[item] = counts[item] + 1
        else:
            counts[item] = 1
    return counts


def reverse_dict(dict):
    reversed_dict = {}
    for key, value in dict.items():
        reversed_dict[value] = key
    return reversed_dict