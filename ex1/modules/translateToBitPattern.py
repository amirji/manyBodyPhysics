def convert(x):
    n = x - x%2
    x = x%2
    while (x >= 2):
        n.append(x - x%2)
        x = x%2
    return n
