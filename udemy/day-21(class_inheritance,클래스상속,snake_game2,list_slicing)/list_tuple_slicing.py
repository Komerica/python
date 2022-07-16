# This method of slicing not only works with List but also works with Tuple!

print("""𝗹𝗶𝘀𝘁""")
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
print(piano_keys[-3:-6:-1]) # ['e', 'd', 'c']
print(piano_keys[4:1:-1])   # ['e', 'd', 'c']
print(piano_keys[2:5:2])    # ['c', 'e']
print(piano_keys[-2:-5:-2]) # ['f', 'd']
print(piano_keys[::-1])     # ['g', 'f', 'e', 'd', 'c', 'b', 'a']
print(piano_keys[::-2])     # ['g', 'e', 'c', 'a']

print("""𝘁𝘂𝗽𝗹𝗲""")
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")
print(piano_tuple[2:5])