length = float(input())
width = float(input())
workspace = 70 * 120

reserved = workspace * 3 / 10000
aisle = width * 100 - 100
column = aisle // 70
row = (length * 100) // 120
available_workspace = column * row - reserved

print(int(available_workspace))
