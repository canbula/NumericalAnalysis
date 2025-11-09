from typing import Any, Dict, List

def remove_duplicates(seq: List[Any]) -> List[Any]:
    out, seen = [], set()
    for x in seq:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out

def list_counts(seq: List[Any]) -> Dict[Any, int]:
    counts: Dict[Any, int] = {}
    for x in seq:
        counts[x] = counts.get(x, 0) + 1
    return counts

def reverse_dict(d: Dict[Any, Any]) -> Dict[Any, List[Any]]:
    rev: Dict[Any, List[Any]] = {}
    for k, v in d.items():
        rev.setdefault(v, []).append(k)
    return rev
