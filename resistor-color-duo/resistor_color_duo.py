def value(colors):
    all_colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

    return int(''.join([str(all_colors.index(color)) for color in colors[:2]]))
