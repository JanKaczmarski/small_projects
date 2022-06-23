"""
    wyrażenie zbioru
"""

names = {"arkadiusz", "Wioletta", "karol", "bartłomiej", "Jakub", "Ania"}


names = {
        name.capitalize()
        for name in names
        if (name[0] == 'b')
}
