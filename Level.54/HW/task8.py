def find_min_max(*args):
    if not args:
        return None, None
    return min(args), max(args)