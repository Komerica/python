# PrettyTable Documentation: https://github.com/jazzband/prettytable
from prettytable import PrettyTable

from prettytable.colortable import ColorTable, Themes
x = ColorTable(theme=Themes.OCEAN)
print(x)

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table.align) # {'base_align_value': 'c', 'Pokemon Name': 'c', 'Type': 'c'}
table.align ="l"
print(table.align) # {'base_align_value': 'c', 'Pokemon Name': 'l', 'Type': 'l'}

print(table)



