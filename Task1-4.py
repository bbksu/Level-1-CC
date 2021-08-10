def square(grid=5):
    string = ""
    for row in range(0, grid):
        for col in range(0, grid + 1):
            if col > grid - grid:
                string+="#"
            else:
                string += " "
        string += "\n"
    print(string)
