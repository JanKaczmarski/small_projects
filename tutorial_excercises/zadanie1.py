def sample(number, x, y):
    xy_range = list(range(x, y+1))
    if number in xy_range:
        return True
    else:
        return False
