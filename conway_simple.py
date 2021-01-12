from os import system
import platform
import random
import time
import copy

def clean():
    """
    Clears the console
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')

def grid(col, row):
    outer = []
    inner = []
    for x in range(col):
        for y in range(row):
            status = random.randint(0, 1)
            inner.append(status)
        outer.append(inner)
        inner = []
    return outer


def findNeighbors(grid, x, y):

    outer = []
    inner = []

    for n in range(x):
        neighbors = 0
        for m in range(y):
            if grid[(n - 1) % column][m] == 1:
                neighbors += 1
            if grid[(n + 1) % column][m] == 1:
                neighbors += 1
            if grid[(n - 1) % column][(m - 1) % row] == 1:
                neighbors += 1
            if grid[(n - 1) % column][(m + 1) % row] == 1:
                neighbors += 1
            if grid[(n) % column][(m - 1) % row] == 1:
                neighbors += 1
            if grid[(n) % column][(m + 1) % row] == 1:
                neighbors += 1
            if grid[(n + 1) % column][(m - 1) % row] == 1:
                neighbors += 1
            if grid[(n + 1) % column][(m + 1) % row] == 1:
                neighbors += 1

            inner.append(neighbors)
            neighbors = 0
        outer.append(inner)
        inner = []

    return outer


def nextGrid(old, neighbors, x, y):

    outer = []
    inner = []


    for c in range(x):
        for d in range(y):
            if old[c][d] == 1:
                if neighbors[c][d] < 2 or neighbors[c][d] > 3:
                    inner.append(0)
                else:
                    inner.append(1)
            elif old[c][d] == 0:
                if neighbors[c][d] == 3:
                    inner.append(1)
                else:
                    inner.append(0)

        outer.append(inner)
        inner = []
    return outer


def printGrid(current, col, row):
    for a in range(col):
        for b in range(row):

            if current[a][b] == 0:
                print(" ", end="")
            else:
                print("O", end="")
        print()

if __name__ == "__main__":
    clean()
    row, column = input("enter rows/columns").split("/")
    row, column = int(row), int(column)

    clean()
    oldGrid = grid(column, row)
    while True:

        neighborsList = findNeighbors(oldGrid, column, row)
        newGrid = nextGrid(oldGrid, neighborsList, column, row)
        printGrid(newGrid, column, row)
        oldGrid = copy.deepcopy(newGrid)
        time.sleep(.05)
        clean()





