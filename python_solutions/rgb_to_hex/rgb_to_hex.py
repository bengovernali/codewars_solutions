def rgb(r, g, b):
    hex_values = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    hex = ""
    values = [r, g, b]
    for value in values:
        if value <= 0:
            hex += "00"
        elif value >= 255:
            hex += "FF"
        else:
            hex += hex_values[int(value / 16)] + hex_values[value % 16]
    return hex