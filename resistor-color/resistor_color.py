def color_code(color):
    global colors
    colors = {'Black': 0, 'Brown': 1, 'Red': 2, 'Orange': 3, 'Yellow': 4, 'Green': 5, 'Blue': 6, 'Violet': 7, 'Grey': 8, 'White': 9}
    return colors[color.capitalize()]


def colors():
    return [k.lower() for k in colors]
