def remove_duplicates(seq: list) -> list:
    no_duplicate = set()
    result = []
    for i in seq:
        if i not in no_duplicate:
            no_duplicate.add(i)
            result.append(i)
    return result

def list_counts(seq: list) -> dict:
    counts = {}
    for i in seq:
        counts[i]=counts.get(i, 0) + 1
    return counts

def reverse_dict(d: dict)->dict:
    return {value: key for key, value in d.items()}
