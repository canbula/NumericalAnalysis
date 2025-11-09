def remove_duplicates(seq: list) -> list:
    return list(set(seq))
def lists_counts(seq: list) -> dict:
    my_dict = dict()
    my_dict = my_dict.fromkeys(seq,0)
    for i in seq:
        my_dict[i]+=1
    return my_dict
def reverse_dict(d: dict) ->dict:
    return {v: k for k, v in d.items()}
