def score(x, y):
    center_distance = (x**2 + y**2)**(1/2)
    if center_distance <= 1:
        return 10
    elif center_distance <= 5:
        return 5
    elif center_distance <= 10:
        return 1
    return 0
